import logging
from os import name
from typing import Any, List
import asyncio

from fastapi.param_functions import Query

from app.schemas import WebSocketAnswer, Tag, Token
from app.core.config import settings
from fastapi import APIRouter, Query, HTTPException, Header, Request
from fastapi.security.api_key import APIKey
from fastapi.responses import Response

from app.tasks.write_tag_task import writetag


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/writeTag",
    response_model=WebSocketAnswer,
    status_code=200,
)
async def write_tag_value_api(tag: Tag,
    access_token: str = Header('', max_lenght=settings.TOKEN_MAX_LEN)
) -> Any:
    """
    write value of some parameter by name
    """

    logger.info(access_token)
    logger.info(f'write_tag {tag}')
    if tag is None:
            raise HTTPException(
                status_code=404,
                detail=str("Recived data is empty"),
            )
    try:
        token = Token(value=access_token)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    response = await writetag(tag, token)
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.response,
        )
    return None