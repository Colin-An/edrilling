from typing import Any

from app.core.config import settings
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

API_KEY_NAME = "access_token"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_header: str = Security(api_key_header),
) -> Any:
    if api_key_header == settings.SECRET_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail=f"API of {settings.PROJECT_NAME} key is not valid!"
        )