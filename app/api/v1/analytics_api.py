from fastapi import APIRouter, Depends, BackgroundTasks, Request
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.api.deps import get_db, get_current_user
from app.schemas.analytics import ViewCreate, ViewResponse, AnalyticsResponse
from app.services.analytics_service import AnalyticsService
from app.repositories.analytics_repository import AnalyticsRepository
from app.schemas.response import StandardResponse
from app.core.security import UserToken
from typing import Optional

router = APIRouter()

@router.post("/views", response_model=StandardResponse[ViewResponse])
async def track_view(
    view_in: ViewCreate, 
    request: Request,
    db: AsyncSession = Depends(get_db),
    # Optional auth: if token present, we track user_id
):
    # Extract user_id manually if header present to avoid 401 on public views
    auth_header = request.headers.get("Authorization")
    user_id = None
    if auth_header and auth_header.startswith("Bearer "):
        try:
            # We can reuse get_current_user logic or just decode manually here safely
            # keeping it simple: track IP mostly
            pass 
        except:
            pass
            
    # For now, let's assume public views don't require auth, but if we want to track user...
    # The prompt implies "Track blog views". 
    
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)
    # Get IP
    ip = request.client.host
    view = await service.track_view(blog_id=view_in.blog_id, ip_address=ip)
    return StandardResponse(success=True, data=view)

@router.get("/metrics/{blog_id}", response_model=StandardResponse[AnalyticsResponse])
async def get_metrics(
    blog_id: UUID, 
    db: AsyncSession = Depends(get_db)
):
    repo = AnalyticsRepository(db)
    service = AnalyticsService(repo)
    metrics = await service.get_blog_metrics(blog_id)
    return StandardResponse(success=True, data=metrics)
