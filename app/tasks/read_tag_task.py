from app.schemas import Tag, WebSocketAnswer
from app.web_socets.ws_functions import produce
from app.core.config import settings

host = settings.WS_HOST

async def readtag(tag: Tag, access_token: str) -> WebSocketAnswer:
    message = f'read|{tag.name}'
    response_text = await produce(message, f"{host}{access_token}")
    return WebSocketAnswer(
        response=response_text
    )
