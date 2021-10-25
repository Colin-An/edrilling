import websockets

async def produce(message: str, host: str) -> str:
    async with websockets.connect(f"wss://{host}") as ws:
        await ws.send(message)
        answer = await ws.recv()
    return answer