from typing import Optional
from pydantic import BaseModel, validator
from app.core.config import settings

class Token(BaseModel):
    value: str

    @validator('value')
    def name_check_lenghts(cls, v):
        if len(v) > settings.TOKEN_MAX_LEN:
            raise ValueError('Lenghts of access_token is too big')
        if len(v) > 8 and 'Bearer ' != v[:7]:
            raise ValueError("access_token doesn't catch format [Bearer $TOKEN]")
        else:
            v = v.replace('Bearer ', '')
        return v