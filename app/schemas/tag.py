from typing import Optional
from pydantic import BaseModel, validator
from app.core.config import settings

# describing what is a tag
class Tag(BaseModel):
    name: str
    value: Optional[float]

    @validator('name')
    def name_check_lenghts(cls, v):
        # may be we can add some other rules, these are just for example
        if len(v) > settings.STR_MAX_LEN:
            raise ValueError('Lenghts of tag name is too big')
        if len(v) == 0:
            raise ValueError('Lenghts of tag name is zero')
        return v

    # this is an eample of data, how it can look like
    class Config:
        schema_extra = {
            "example": {
                "name": "ConfigData.bit.totalFlowArea",
                "value": 0.123,
            }
        }