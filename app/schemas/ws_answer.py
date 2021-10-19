from pydantic import BaseModel

class WebSocketAnswer(BaseModel):
    response: str