from schemas import Tag, WebSocketAnswer

async def readtag(tag: Tag) -> WebSocketAnswer:
    tag.value = 0.999
    print(tag)
    answer = WebSocketAnswer(
        response = 'blablabla'
    ) 
    print(answer)
    return answer