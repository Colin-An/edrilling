import logging
from os import name
from typing import Any, List
import asyncio

from fastapi.param_functions import Query

from app.schemas import WebSocketAnswer, Tag
from app.api import deps
from fastapi import APIRouter, Query, HTTPException, Header, Request
from fastapi.security.api_key import APIKey
from fastapi.responses import Response

from app.tasks.read_tag_task import readtag


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/writeTag",
    response_model=WebSocketAnswer,
    status_code=200,
)
async def write_tag_value_api(data: Tag,
    access_token: str = Header('', max_lenght=500)
) -> Any:
    """
    write value of some parameter by name
    """
    if not (access_token and name):
        raise HTTPException(
            status_code=400,
            detail="Bad parameter name or access_token",
        )
    logger.info(access_token)
    logger.info('read_tag request')
    results = await readtag(Tag(name=name))
    return results