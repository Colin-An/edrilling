from starlette import status
import websockets
from websockets.exceptions import WebSocketException
from asyncio.exceptions import TimeoutError
from app.schemas import WebSocketAnswer
import asyncio
from app.core.config import settings


async def produce(message: str, host: str, wait_answer=True) -> WebSocketAnswer:
    try:
        async with websockets.connect(f"wss://{host}") as ws:
            await ws.send(message)
            if wait_answer:
                answer = await asyncio.wait_for(ws.recv(), timeout=settings.TIMEOUT)
            else:
                answer = ''
    except (WebSocketException, TimeoutError) as e:
        return WebSocketAnswer(
            response=str(e),
            status_code=404
        )
    return WebSocketAnswer(
            response=answer,
            status_code=200
        )