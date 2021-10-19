from schemas import Tag, WebSocketAnswer

async def readtag(tag: Tag) -> WebSocketAnswer:
    answer = WebSocketAnswer(
        response = tag.name + ' bla'
    ) 
    return answer