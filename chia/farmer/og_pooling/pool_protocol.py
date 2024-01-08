from dataclasses import dataclass
from typing import Optional

from chia_rs import G2Element

from chia.types.blockchain_format.proof_of_space import ProofOfSpace
from chia.types.blockchain_format.sized_bytes import bytes32
from chia.util.ints import uint64, uint32
from chia.util.streamable import streamable, Streamable


@streamable
@dataclass(frozen=True)
class PartialPayloadOG(Streamable):
    id: str
    difficulty: uint64
    proof_of_space: ProofOfSpace
    sp_hash: bytes32
    end_of_sub_slot: bool
    total_plots: uint32  # Total number of plots on this farmer
    payout_address: str  # The farmer can choose where to send the rewards
    harvester_id: Optional[bytes32]


@streamable
@dataclass(frozen=True)
class SubmitPartialOG(Streamable):
    payload: PartialPayloadOG
    aggregate_signature: G2Element  # Sig of partial by plot key and pool key
