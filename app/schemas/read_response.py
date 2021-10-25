from pydantic import BaseModel

class ReadResponse(BaseModel):
    response: str