from fastapi import APIRouter
from app.api.v1 import analytics_api

api_router = APIRouter()
api_router.include_router(analytics_api.router, prefix="/analytics", tags=["analytics"])
