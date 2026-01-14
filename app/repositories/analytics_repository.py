from uuid import UUID
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.analytics import BlogView

class AnalyticsRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def log_view(self, view: BlogView) -> BlogView:
        self.session.add(view)
        await self.session.commit()
        await self.session.refresh(view)
        return view

    async def get_views_count(self, blog_id: UUID) -> int:
        stmt = select(func.count(BlogView.id)).where(BlogView.blog_id == blog_id)
        result = await self.session.execute(stmt)
        return result.scalar_one() or 0
