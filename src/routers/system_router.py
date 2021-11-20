from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from services.tor_service import TorService, get_service

router = APIRouter()


def tor_service():
    return get_service()


@router.get("/healthz")
async def health():
    return {"ok": True}


@router.get("/")
async def get_operation_quantity(service: TorService = Depends(tor_service)):
    return {"ok": True, "count": service.count}


@router.get("/log")
async def get_operation_log(service: TorService = Depends(tor_service)):
    return HTMLResponse(service.log)
