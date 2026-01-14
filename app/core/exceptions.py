from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.response import StandardResponse, ErrorDetail

async def global_exception_handler(request: Request, exc: Exception):
    error = ErrorDetail(
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected error occurred."
    )
    return JSONResponse(
        status_code=500,
        content=StandardResponse(success=False, error=error).model_dump(mode='json')
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    error = ErrorDetail(
        code=str(exc.status_code),
        message=str(exc.detail)
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=StandardResponse(success=False, error=error).model_dump(mode='json')
    )
