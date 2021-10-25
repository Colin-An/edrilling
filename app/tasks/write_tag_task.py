import logging
from time import time

from app.schemas import Tag, WebSocketAnswer, Token
from app.web_socets.ws_functions import produce
from app.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

host = settings.WS_HOST
port = settings.WS_PORT
path = settings.WS_PATH

async def writetag(tag: Tag, access_token: Token) -> WebSocketAnswer:
    message = f'write|{tag.name}|{round(time()*1000.0)}|6|{tag.value}'
    url = f'{host}:{port}/{path}'
    logger.info(f'sending message {message} to {url}')
    response = await produce(
                    message,
                    f"{url}?access_token={access_token.value}", 
                    False)
    return response
