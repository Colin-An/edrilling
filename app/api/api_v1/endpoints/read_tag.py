import logging
from os import name
from typing import Any, List
import asyncio

from fastapi.param_functions import Query
from app.core.config import settings

from app.schemas import Tag, Token, ReadResponse
from fastapi import APIRouter, Query, HTTPException, Header


from app.tasks.read_tag_task import readtag


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/readTag",
    response_model=ReadResponse,
    status_code=200,
)
async def read_tag_value_api(name: str = Query('', max_lenght=settings.STR_MAX_LEN),
    access_token: str = Header('', max_lenght=settings.TOKEN_MAX_LEN)
) -> Any:
    """
    read value of some parameter by name
    """
    logger.info(f'access_token {access_token}')
    logger.info(f'read_tag {name}')

    try:
        tag = Tag(name=name)
        token = Token(value=access_token)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    ws_results = await readtag(tag, token)

    if "read_error" in ws_results.response or ws_results.status_code != 200:
        raise HTTPException(
            status_code=404,
            detail=ws_results.response,
        )
    return ReadResponse(response=ws_results.response)
    
