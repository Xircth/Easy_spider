from fastapi import APIRouter,Depends
from app.utils.result import ApiResponse
import os
from sqlalchemy.orm import Session
from app.core.tools.read_tasks import read_tasks,_get_task_by_id,read_logs
from app.service.task_invoke import start_task
from app.service.task_service import TaskService
from app.database import get_db
from typing import Generator

router = APIRouter(prefix="/plugin", tags=["plugin"])
# 移除全局 taskService 变量，改为每次请求创建新实例

@router.get("/test")
def test_endpoint():
    return ApiResponse.success("hello world wow")

@router.get("/list")
def list():
    task_list = read_tasks()
    return ApiResponse.success(task_list)


@router.get("/task")
def get_task_by_id(id):
    task = _get_task_by_id(id)
    return ApiResponse.success(task)
    

@router.post("/invoke")
def invoke_task(id):
    eid = start_task(id)
    return ApiResponse.success(eid)

@router.get("/logs")
def read_task_logs(id,save_name):
    logs = read_logs(id,50,save_name)
    return ApiResponse.success(logs)

@router.get("/status")
def task_status(E_id, db: Session = Depends(get_db)):
    taskService = TaskService(db=db)
    if taskService is None:
        taskService = TaskService(db=db)
        # 确保每次请求都使用最新的数据库会话
        if taskService.db != db:
            taskService.db = db
    # db = next(get_db())
    status = taskService.get_task_status_by_task_E_id(task_E_id=E_id)
    return ApiResponse.success(status)

def stop_task(E_id):
    pass