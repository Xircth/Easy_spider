from fastapi import APIRouter,Depends
from app.utils.result import ApiResponse
import os
from app.core.tools.read_tasks import read_tasks

router = APIRouter(prefix="/plugin", tags=["plugin"])

@router.get("/test")
def test_endpoint():
    return ApiResponse.success("hello world wow")

@router.get("/list")
def list():
    task_list = read_tasks()
    return ApiResponse.success(task_list)

@router.post("/invoke")
def invoke_task(id):
    
    pass

@router.get("/logs")
def read_task_logs(E_id):
    pass