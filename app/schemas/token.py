from typing import Optional
from pydantic import BaseModel, validator
from app.core.config import settings

# separate class for token
class Token(BaseModel):
    value: str

    @validator('value')
    def name_check_lenghts(cls, v):
        # some checks for example
        if len(v) > settings.TOKEN_MAX_LEN:
            raise ValueError('Lenghts of access_token is too big')
        if len(v) > 8 and 'Bearer ' != v[:7]:
            raise ValueError("access_token doesn't catch format [Bearer $TOKEN]")
        else:
            # delete first part of token for using in web socket connection
            v = v.replace('Bearer ', '')
        return v