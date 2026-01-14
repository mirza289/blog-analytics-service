from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class ViewCreate(BaseModel):
    blog_id: UUID

class ViewResponse(BaseModel):
    id: UUID
    blog_id: UUID
    viewed_at: datetime
    
    class Config:
        from_attributes = True

class AnalyticsResponse(BaseModel):
    blog_id: UUID
    total_views: int
