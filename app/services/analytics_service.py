from uuid import UUID
from typing import Optional
from app.repositories.analytics_repository import AnalyticsRepository
from app.models.analytics import BlogView

class AnalyticsService:
    def __init__(self, repo: AnalyticsRepository):
        self.repo = repo

    async def track_view(self, blog_id: UUID, user_id: Optional[UUID] = None, ip_address: Optional[str] = None) -> BlogView:
        view = BlogView(blog_id=blog_id, user_id=user_id, ip_address=ip_address)
        return await self.repo.log_view(view)

    async def get_blog_metrics(self, blog_id: UUID):
        count = await self.repo.get_views_count(blog_id)
        return {"blog_id": blog_id, "total_views": count}
