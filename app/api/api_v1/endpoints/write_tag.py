import logging
from typing import Any

from app.core.config import settings
from app.tasks.write_tag_task import write_tag
from app.schemas import Tag, Token

from fastapi import APIRouter, HTTPException, Header


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/writeTag",
    response_model=None,
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

    # check that input data is not empty
    if tag is None:
            raise HTTPException(
                status_code=404,
                detail=str("Recived data is empty"),
            )
    try:
        # create Token object from input data
        token = Token(value=access_token)
    except ValueError as e:
        # if some troubles with validation, create 404 error (but it will be 
        # better to use code 400, like "bad request")
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
    ws_results = await write_tag(tag, token)
    # check if smth happend during connection or sending
    if ws_results.status_code != 200:
        raise HTTPException(
            status_code=ws_results.status_code,
            detail=ws_results.response,
        )
    # if everuthing is OK return nothing as in a task
    return None