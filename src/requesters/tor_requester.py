from typing import List, Optional

import aiohttp
from aiohttp_socks import ProxyConnector

from settings import Settings


class TorRequester:
    def __init__(self, checker_address: str):
        self._checker_address = checker_address
        self._server = Settings.SERVER_ADDRESS

    @property
    def connector(self):
        return ProxyConnector.from_url(Settings.TOR_ADDRESS, rdns=True)

    async def get(
        self,
        session,
        *,
        url: str,
        headers: Optional[str] = None,
        params: Optional[dict] = None,
    ):
        async with session.get(url, headers=headers, params=params) as res:
            return await res.json()

    async def put(
        self,
        session,
        *,
        url: str,
        headers: Optional[str] = None,
        data: Optional[dict] = None,
    ):
        async with session.put(url, headers=headers, json=data) as res:
            return await res.json()

    async def get_users(self, count=Settings.TOTAL_EMAILS):
        async with aiohttp.ClientSession(connector=self.connector) as session:
            return await self.get(
                session, url=f"{self._server}/getUsers", params={"count": count}
            )

    async def check_emails(self, email: str):
        async with aiohttp.ClientSession(connector=self.connector) as session:
            return await self.get(
                session,
                url=f"{self._checker_address}/checkUser",
                params={"email": email},
            )

    async def update_emails(self, emails: List[str], state: int):
        async with aiohttp.ClientSession(connector=self.connector) as session:
            return await self.put(
                session,
                url=f"{self._server}/updateUsers",
                data={"emails": emails, "state": state},
            )
