import asyncio
import logging
import time
from logging import Logger
from typing import Any, Optional, Dict

from aiohttp import ClientSession, ClientTimeout, ClientError, ClientConnectionError
from aiohttp.typedefs import StrOrURL

from chia import __version__
from chia.farmer.og_pooling.pool_protocol import SubmitPartialOG
from chia.server.server import ssl_context_for_root
from chia.ssl.create_ssl import get_mozilla_ca_crt

timeout = ClientTimeout(total=30)

partial_timeout = ClientTimeout(total=30, sock_read=8.5, sock_connect=8.5)
partial_log = logging.getLogger("partial_post")


async def post_partial(url: StrOrURL, *, data: Any = None, **kwargs: Any) -> Dict:
    ttl = time.time() + 23
    last_error: Optional[ClientError] = None
    while time.time() < ttl:
        try:
            async with ClientSession(timeout=partial_timeout) as client:
                async with client.post(url, data=data, **kwargs) as res:
                    if res.ok:
                        return await res.json()
                    else:
                        last_error = ClientConnectionError(f"Partial submit resp not ok: {url}, {res.status}")
                        break
        except ClientError as e:
            partial_log.error(f"Partial submit error: {e}")
            last_error = e
    raise last_error if last_error else ClientConnectionError(f"No partial submitted to {url}")


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

    async def submit_partial(self, submit_partial: SubmitPartialOG) -> Dict:
        return await post_partial(f"{self.base_url}/og/partial",
                                  json=submit_partial.to_json_dict(),
                                  ssl=ssl_context_for_root(get_mozilla_ca_crt(), log=self.log),
                                  headers={"User-Agent": f"Chia Blockchain v.{__version__}"},
                                  )
