from app.schemas import Tag, WebSocketAnswer
import asyncio

async def readtag(tag: Tag) -> WebSocketAnswer:
    answer = WebSocketAnswer(
        response = tag.name + ' bla'
    )
    await asyncio.sleep(1)
    return answer