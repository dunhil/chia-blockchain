from logging import Logger

from aiohttp import ClientSession, ClientTimeout

from chia.farmer.og_pooling.pool_protocol import SubmitPartialOG
from chia.server.server import ssl_context_for_root
from chia.ssl.create_ssl import get_mozilla_ca_crt

timeout = ClientTimeout(total=30, sock_connect=5, sock_read=5)


class PoolApiClient:
    base_url: str

    def __init__(self, base_url: str, log: Logger) -> None:
        self.base_url = base_url
        self.log = log

    async def get_pool_info(self):
        async with ClientSession(timeout=timeout) as client:
            async with client.get(f"{self.base_url}/og/pool_info",
                                  ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                                  ) as res:
                return await res.json()

    async def submit_partial(self, submit_partial: SubmitPartialOG):
        async with ClientSession(timeout=timeout) as client:
            async with client.post(f"{self.base_url}/og/partial",
                                   json=submit_partial.to_json_dict(),
                                   ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                                   ) as res:
                return await res.json()
