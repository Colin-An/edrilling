from api.api_v1.endpoints import read_tag, service
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(service.router, prefix="/service", tags=["service"])
api_router.include_router(read_tag.router, prefix="/tag", tags=["readtag"])
