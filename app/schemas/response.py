from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

T = TypeVar("T")

class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None

class MetaData(BaseModel):
    requestId: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StandardResponse(BaseModel, Generic[T]):
    success: bool
    data: Optional[T] = None
    error: Optional[ErrorDetail] = None
    meta: MetaData = Field(default_factory=lambda: MetaData(requestId=str(uuid.uuid4())))
