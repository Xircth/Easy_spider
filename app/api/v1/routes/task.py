from fastapi import APIRouter,Depends
from app.utils.result import ApiResponse
import os
from app.core.tools.read_tasks import read_tasks
from app.core.security import get_current_user

router = APIRouter(prefix="/plugin", tags=["plugin"])

@router.get("/test")
def test_endpoint():
    return ApiResponse.success("hello world wow")

@router.get("/list")
def test():
    task_list = read_tasks()
    return ApiResponse.success(task_list)

@router.post("/invoke")
def invoke_task(id):
    
    pass