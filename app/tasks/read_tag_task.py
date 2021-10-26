import logging

from app.schemas import Tag, WebSocketAnswer, Token
from app.web_socets.ws_functions import produce
from app.core.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

host = settings.WS_HOST
port = settings.WS_PORT
path = settings.WS_PATH

async def read_tag(tag: Tag, access_token: Token) -> WebSocketAnswer:
    # create message with right format
    message = f'read|{tag.name}'
    # create ULR to web socket server
    url = f'{host}:{port}/{path}'
    logger.info(f'sending message {message} to {url}')
    # send message to server with access_token
    response = await produce(
        message, 
        f"{url}?access_token={access_token.value}")
    return response
