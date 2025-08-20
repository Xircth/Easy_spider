from fastapi import APIRouter
from app.api.v1.routes import test_router

api_router = APIRouter()
api_router.include_router(test_router)