from app.api.api_v1.endpoints import read_tag, service, write_tag
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(service.router, prefix="/service", tags=["service"])
api_router.include_router(read_tag.router, prefix="/tag", tags=["readtag"])
api_router.include_router(write_tag.router, prefix="/tag", tags=["writetag"])
