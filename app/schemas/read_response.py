from pydantic import BaseModel

# model for answer after success reading
class ReadResponse(BaseModel):
    response: str