import asyncio
from datetime import datetime
from typing import List

import inject

from requesters.tor_requester import TorRequester
from settings import Settings

service = None


@inject.autoparams()
def get_service(requester: TorRequester):
    global service
    if service is None:
        service = TorService(requester)
    return service


class TorService:
    @inject.autoparams()
    def __init__(self, requester: TorRequester):
        self._requester = requester

        self.count = 0
        self.log = "OPERATION LOG: <br>"

    async def periodic_task(self):

        while True:
            try:
                await self.update_emails()
            except ValueError:
                self.count += 1
                await asyncio.sleep(Settings.RAISE_TIMEOUT)
            else:
                self.count += 1
                await asyncio.sleep(Settings.TIMEOUT)

    async def update_emails(self):
        users = await self._get_users()
        checked_emails = await self._check_emails([user["email"] for user in users])
        updated_data = await self._handle_emails(checked_emails)
        await self._update_emails(updated_data)

    async def _get_users(self):
        if result := await self._requester.get_users():
            return result
        raise ValueError

    async def _check_emails(self, emails: List[str]):
        return await asyncio.gather(
            *[self._requester.check_emails(email) for email in emails]
        )

    async def _handle_emails(self, emails: List[dict[str, bool]]):
        result = {1: [], 0: []}
        for email_data in emails:
            for email, isRegister in email_data.items():
                if isRegister:
                    result[1].append(email)
                else:
                    result[0].append(email)
        return result

    async def _update_emails(self, update_data: dict[int, List[str]]):
        self.log += f"""
        {datetime.utcnow()}: <br> 
        {await self._requester.update_emails(update_data[1], 1)} <br>
        {await self._requester.update_emails(update_data[0], 0)} <br>
         <br> <br>
        """
