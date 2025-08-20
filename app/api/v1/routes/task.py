from fastapi import APIRouter
from app.utils.result import ApiResponse



router = APIRouter(prefix="/plugin", tags=["plugin"])

@router.get("/list")
def test_endpoint():
    
    return ApiResponse.success("hello world wow")

