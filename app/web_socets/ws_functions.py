from starlette import status
import websockets
from websockets.exceptions import WebSocketException
from asyncio.exceptions import TimeoutError
from app.schemas import WebSocketAnswer
import asyncio
from app.core.config import settings


async def produce(message: str, url: str, wait_answer=True) -> WebSocketAnswer:
    """sending message to web socket server

    In async way thus function try to connect to web socket server and
    send mesage. After that, this function await for answer some number of 
    seconds if special flag is True and return result or error message with
    404 status code (because of the task)

    Args:
        message: String message to web socket server in a special format
        url: url which include host:port/some_path?access_token=[token] 
        wait_answer: Optional; Do we await for answer from web socket server 
            side or not

    Returns:
        WebSocketAnswer object
        example:

        {
            "response": "read|ConfigData.bit.totalFlowArea|0|6|0.59||GOOD",
            "status_code": 200
        }

    Raises:
        WebSocketException: Any troubles with connection to websocket server, 
            because it is a base exception class for websockets functionality
        TimeoutError: rised when server doesn't send response more than 
            number of seconds in environment TIMEOUT variable
    """
    try:
        # connect to server in context manager
        async with websockets.connect(f"wss://{url}") as ws:
            # sending message
            await ws.send(message)
            # receive answer if it is necessary
            if wait_answer:
                answer = await asyncio.wait_for(ws.recv(), timeout=settings.TIMEOUT)
            else:
                answer = ''
    except (WebSocketException, TimeoutError) as e:
        return WebSocketAnswer(
            response=str(e),  # send description of trouble
            status_code=404  # code 404 as in the task
        )
    return WebSocketAnswer(
            response=answer,
            status_code=200
        )