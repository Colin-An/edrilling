import logging
from os import name
from typing import Any
import asyncio

from app.schemas import WebSocketAnswer, Tag
from app.schemas.ws_answer import WebSocketAnswer
from fastapi import APIRouter
from fastapi.security.api_key import APIKey
from fastapi.responses import JSONResponse

from app.tasks.read_tag_task import readtag


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/read",
    response_model=WebSocketAnswer,
    status_code=200,
)
async def read_tag_value_api(tag_name: str
        #task_id: str, api_key: APIKey = Depends(deps.get_api_key)
) -> Any:
    """
    read value of some parameter by name
    """
    logger.info('read_tag request')
    results = await readtag(Tag(name=tag_name))
    return results
