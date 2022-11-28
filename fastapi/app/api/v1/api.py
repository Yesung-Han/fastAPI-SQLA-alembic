from fastapi import APIRouter

from app.api.v1.endpoints import teacher

api_router = APIRouter()

api_router.include_router(teacher.router, prefix="/teachers", tags=["users"])