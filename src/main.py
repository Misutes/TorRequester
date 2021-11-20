import asyncio
import logging

import inject
from fastapi import FastAPI

from requesters.tor_requester import TorRequester
from routers.system_router import router as system_router
from services.tor_service import get_service
from settings import Settings

app = FastAPI()
app.include_router(system_router)
periodic_task = None


def config(binder):
    requester = TorRequester(Settings.CHECKER_ADDRESS)
    binder.bind(TorRequester, requester)


@app.on_event("startup")
async def startup():
    global periodic_task
    inject.configure(config)

    service = get_service()
    periodic_task = asyncio.create_task(service.periodic_task())


@app.on_event("shutdown")
async def shutdown():
    global periodic_task
    periodic_task.cancel()
    await periodic_task

    logging.info("App is closed")
