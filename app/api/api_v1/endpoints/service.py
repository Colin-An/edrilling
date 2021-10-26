import logging
from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.config import settings
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# endpoint for checking server
@router.get("/getServiceInfo/", status_code=200)
async def get_service_info() -> JSONResponse:
    """
    Get information about server status 
    """
    server_status = jsonable_encoder(
        {
            "service": settings.PROJECT_NAME,
            "version": settings.PUBLIC_VERSION,
            "time": datetime.now(timezone(timedelta(hours=3))).strftime(
                "%d.%m.%Y %H:%M:%S"
            ),
            "status": "OK",
        }
    )
    return JSONResponse(content=server_status)


@router.post("/TestTask/", status_code=200)
async def test_task(data: str, request: Request) -> Any:
    """
    just tests
    """
    logger.info(f"REQUEST CLIENT: {request.client}")
    logger.info(f"REQUEST HEADERS: {request.headers}")
    logger.info(f"REQUEST ITEMS: {request.items}")
    logger.info(f"REQUEST QUERY PARAMS: {request.query_params}")
    logger.info(f"REQUEST PATH PARAMS: {request.path_params}")
    # logger.info(f"REQUEST JSON: {await request.json()}")
    logger.info(f"REQUEST BODY: {await request.body()}")
    logger.info(f"REQUEST DATA: {data}")
    return None
