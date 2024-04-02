import asyncio
import logging
import time
from typing import Optional, Dict, Tuple, Any

from chia_rs import G1Element, G2Element, AugSchemeMPL

import chia.server.ws_connection as ws
from chia.consensus.pot_iterations import calculate_sp_interval_iters, calculate_iterations_quality
from chia.farmer.og_pooling.pool_api_client import PoolApiClient
from chia.farmer.og_pooling.pool_protocol import PartialPayloadOG, SubmitPartialOG
from chia.harvester.harvester_api import HarvesterAPI
from chia.protocols import farmer_protocol, harvester_protocol
from chia.types.blockchain_format.proof_of_space import generate_plot_public_key
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.util.bech32m import encode_puzzle_hash
from chia.util.config import load_config, save_config
from chia.util.ints import uint64, uint32

log = logging.getLogger("og_pooling")

DEFAULT_POOL_URL: str = "https://pool.sweetchia.com"
POOL_SUB_SLOT_ITERS: uint64 = uint64(37600000000)


class PoolWorker:
    def __init__(
            self,
            root_path,
            farmer
    ):
        self._root_path = root_path
        # to avoid circular imports
        from chia.farmer.farmer import Farmer
        self.farmer: Farmer = farmer
        self.config = self.farmer.config
        self.log = log

        key = "og_pooling"
        if key not in self.config:
            config_template = {
                "enabled": True,
                "pool_url": DEFAULT_POOL_URL,
            }
            config = load_config(self._root_path, "config.yaml")
            config["farmer"][key] = config_template
            save_config(self._root_path, "config.yaml", config)
            self.config[key] = config_template
            self.log.info(f"config.yaml upgraded for legacy pooling")

        og_config = self.config.get(key)
        self.pool_enabled = og_config.get("enabled", True)
        self.pool_url = og_config.get("pool_url", DEFAULT_POOL_URL)
        self.pool_payout_address: str = str(og_config.get("pool_payout_address", "")).strip()

        self.pool_target: Optional[bytes32] = None
        self.pool_target_encoded: Optional[str] = None

        self.pool_sub_slot_iters = POOL_SUB_SLOT_ITERS
        self.iters_limit = calculate_sp_interval_iters(self.farmer.constants, self.pool_sub_slot_iters)
        self.pool_difficulty: uint64 = uint64(1)
        self.pool_minimum_difficulty: uint64 = uint64(1)
        self.pool_partial_target_time = 5 * 60
        self.last_partial_submit_time: float = time.time()
        self.pool_client: Optional[PoolApiClient] = None
        self.adjust_difficulty_task: Optional[asyncio.Task] = None
        self.total_plots = 0
        self.harvester_plots: Dict = {}

    @property
    def _is_pooling_enabled(self):
        return self.pool_enabled and \
               self.pool_url is not None

    @property
    def _is_pool_connected(self):
        return self.pool_client is not None

    @property
    def _shut_down(self):
        # noinspection PyProtectedMember
        return self.farmer._shut_down

    async def _connect_to_pool(self):
        pool_info: Dict = {}
        has_pool_info = False

        client = PoolApiClient(self.pool_url, self.farmer.log)
        self.log.info(f"Connecting to pool {client.base_url}")
        while not self._shut_down and not has_pool_info:
            try:
                pool_info = await client.get_pool_info()
                has_pool_info = True
            except Exception as e:
                self.log.error(f"Error retrieving pool info: {e}")
                await asyncio.sleep(5)

        if self._shut_down:
            return

        pool_name = pool_info["name"]
        self.log.info(f"Connected to pool {pool_name}")
        self.pool_minimum_difficulty = pool_info["minimum_difficulty"]
        self.pool_difficulty = self.pool_minimum_difficulty
        self.pool_partial_target_time = pool_info["partial_target_time"]

        self.pool_target = bytes32.from_hexstr(pool_info["target_puzzle_hash"])
        address_prefix = self.config["network_overrides"]["config"][self.config["selected_network"]]["address_prefix"]
        self.pool_target_encoded = encode_puzzle_hash(self.pool_target, address_prefix)

        if self.farmer.pool_target is not self.pool_target or \
                self.farmer.pool_target_encoded is not self.pool_target_encoded:
            # self.farmer.set_reward_targets(farmer_target_encoded=None, pool_target_encoded=pool_target_encoded)
            self.farmer.pool_target = self.pool_target
            self.farmer.pool_target_encoded = self.pool_target_encoded
        self.pool_client = client

        self.log.info(f"Pool info: {pool_name}, cur_diff={self.pool_difficulty}, "
                      f"target_time={self.pool_partial_target_time}, "
                      f"target_hash={self.pool_target_encoded}")

    async def _initialize_and_adjust_difficulty_task(self):
        last_tick = time.time()
        while not self._shut_down:
            await asyncio.sleep(1)
            now = time.time()
            if now - last_tick < 60:
                continue
            last_tick = now
            elapsed = now - self.last_partial_submit_time
            if elapsed < self.pool_partial_target_time or self.pool_partial_target_time < 1:
                continue
            missing_partials = elapsed // self.pool_partial_target_time
            new_difficulty = int(max(
                (self.pool_difficulty - (missing_partials * 2)),
                int(self.pool_minimum_difficulty)
            ))
            if new_difficulty == self.pool_difficulty:
                continue
            old_difficulty = self.pool_difficulty
            self.pool_difficulty = new_difficulty
            self.log.warning(
                f"Lowered the legacy pool difficulty {old_difficulty} => {new_difficulty} due to no partial submits "
                f"within the last {int(round(elapsed))} seconds"
            )

    async def start(self):
        if self._is_pooling_enabled:
            await self._connect_to_pool()
            self.adjust_difficulty_task = asyncio.create_task(self._initialize_and_adjust_difficulty_task())
        else:
            self.log.info(f"Legacy pooling disabled")

    async def close(self):
        if self.adjust_difficulty_task is not None:
            await self.adjust_difficulty_task
        self.pool_client = None

    def new_signage_point(self, new_signage_point: farmer_protocol.NewSignagePoint) -> Tuple[uint64, uint64]:
        if self._is_pool_connected:
            self.total_plots = sum(self.harvester_plots.values())
            self.harvester_plots = {}
            return uint64(self.pool_difficulty), self.pool_sub_slot_iters
        else:
            return new_signage_point.difficulty, new_signage_point.sub_slot_iters

    def farming_info(self, request: farmer_protocol.FarmingInfo, peer: ws.WSChiaConnection):
        if self._is_pool_connected:
            self.harvester_plots[peer.peer_node_id] = request.total_plots

    def get_pool_target(self) -> bytes32:
        if self._is_pool_connected:
            return self.pool_target
        else:
            return self.farmer.pool_target

    def get_pool_target_encoded(self) -> str:
        if self._is_pool_connected:
            return self.pool_target_encoded
        else:
            return self.farmer.pool_target_encoded

    async def new_proof_of_space(
            self,
            new_proof_of_space: harvester_protocol.NewProofOfSpace,
            peer: ws.WSChiaConnection,
            pool_public_key: G1Element,
            computed_quality_string: bytes32
    ):
        if not self._is_pool_connected:
            return

        required_iters = calculate_iterations_quality(
            self.farmer.constants.DIFFICULTY_CONSTANT_FACTOR,
            computed_quality_string,
            new_proof_of_space.proof.size,
            self.pool_difficulty,
            new_proof_of_space.sp_hash,
        )
        if required_iters >= self.iters_limit:
            self.log.info(
                f"Proof of space not good enough for pool difficulty of {self.pool_difficulty}"
            )
            return

        # Submit partial to pool
        payout_address = self.pool_payout_address if self.pool_payout_address else self.farmer.farmer_target_encoded
        is_eos = new_proof_of_space.signage_point_index == 0
        payload = PartialPayloadOG(
            self.farmer.server.node_id,
            self.pool_difficulty,
            new_proof_of_space.proof,
            new_proof_of_space.sp_hash,
            is_eos,
            uint32(self.total_plots),
            payout_address,
            peer.peer_node_id,
        )

        # The plot key is 2/2 so we need the harvester's half of the signature
        m_to_sign = payload.get_hash()
        request = harvester_protocol.RequestSignatures(
            new_proof_of_space.plot_identifier,
            new_proof_of_space.challenge_hash,
            new_proof_of_space.sp_hash,
            [m_to_sign],
            message_data=None,
            rc_block_unfinished=None,
        )
        sign_response: Any = await peer.call_api(HarvesterAPI.request_signatures, request)
        if not isinstance(sign_response, harvester_protocol.RespondSignatures):
            self.log.error(f"Invalid response from harvester: {sign_response}")
            return

        assert len(sign_response.message_signatures) == 1

        plot_signature: Optional[G2Element] = None
        for sk in self.farmer.get_private_keys():
            pk = sk.get_g1()
            if pk == sign_response.farmer_pk:
                agg_pk = generate_plot_public_key(sign_response.local_pk, pk)
                assert agg_pk == new_proof_of_space.proof.plot_public_key
                sig_farmer = AugSchemeMPL.sign(sk, m_to_sign, agg_pk)
                plot_signature = AugSchemeMPL.aggregate([sig_farmer, sign_response.message_signatures[0][1]])
                assert AugSchemeMPL.verify(agg_pk, m_to_sign, plot_signature)
        pool_sk = self.farmer.pool_sks_map[bytes(pool_public_key)]
        authentication_signature = AugSchemeMPL.sign(pool_sk, m_to_sign)

        assert plot_signature is not None
        agg_sig: G2Element = AugSchemeMPL.aggregate([plot_signature, authentication_signature])

        submit_partial = SubmitPartialOG(payload, agg_sig)
        self.log.info(f"Submitting partial to pool {self.pool_url}")
        self.last_partial_submit_time = time.time()

        submit_response: Dict
        try:
            submit_response = await self.pool_client.submit_partial(submit_partial)
        except Exception as e:
            self.log.error(f"Error submitting partial to pool {self.pool_url}: {e}")
            return

        self.log.info(f"Pool response: {submit_response}")
        if "new_difficulty" in submit_response:
            new_difficulty = submit_response["new_difficulty"]
            if new_difficulty != self.pool_difficulty:
                self.pool_difficulty = new_difficulty
                self.log.info(f"Pool difficulty changed to {self.pool_difficulty}")

        if "partial_target_time" in submit_response:
            target_time = submit_response["partial_target_time"]
            if target_time >= 0 and target_time != self.pool_partial_target_time:
                self.pool_partial_target_time = target_time
                self.log.info(f"Pool partial target time changed to {self.pool_partial_target_time}")

        if "error_code" in submit_response:
            if submit_response["error_code"] == 5:
                self.log.warning(f"Partial difficulty too low")
            else:
                self.farmer.log.error(
                    f"Error in pooling: {submit_response['error_code']}, "
                    f"{submit_response['error_message']}"
                )
