import logging

from fastapi import FastAPI
from app.core.config import settings
from app.api.api_v1.api import api_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
app.include_router(api_router, prefix=settings.API_V1_STR)

from app.schemas import WebSocketAnswer
a = WebSocketAnswer(response='a')
print(a)
