from pydantic import BaseModel
from typing import Optional

# write string responce to that object, and use status_code if we have
# some troubles with connection or something else
class WebSocketAnswer(BaseModel):
    response: str
    status_code: Optional[int]