from pydantic import BaseModel
from typing import Optional

class WebSocketAnswer(BaseModel):
    response: str
    status_code: Optional[int]