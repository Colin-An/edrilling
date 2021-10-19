import logging
from os import name
from typing import Any
import asyncio

import schemas
from api import deps
from schemas.ws_answer import WebSocketAnswer
from schemas import Tag
from fastapi import APIRouter, Depends
from fastapi.security.api_key import APIKey
from fastapi.responses import JSONResponse

from tasks.read_tag_task import readtag


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/read",
    response_model=schemas.WebSocketAnswer,
    status_code=200,
)
def read_tag_value_api(tag_name: str
        #task_id: str, api_key: APIKey = Depends(deps.get_api_key)
) -> Any:
    """
    read value of some parameter by name
    """
    logger.info('read_tag request')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    answer = loop.run_until_complete(readtag(Tag(
        name = tag_name
    )))
    return answer