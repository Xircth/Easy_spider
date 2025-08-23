from typing import Optional, List
from sqlalchemy.orm import Session
from app.database.models.task import Task
from app.database import get_db
import time
from fastapi import Depends
class TaskService:
    """
    任务服务类，处理任务执行状态相关的业务逻辑
    """
    def __init__(self, db: Session):
        self.db = db
    

    def get_tasks_by_task_id(self, task_id: int) -> List[Task]:
        """
        根据task_id查询该任务下的所有任务执行情况

        Args:
            db: 数据库会话
            task_id: 任务ID

        Returns:
            任务执行情况列表
        """
        db = self.db
        return db.query(Task).filter(Task.task_id == task_id).all()

    def create_task(
        self,
        task_id: int,
        task_E_id: str,
        status: str = "pending"
    ) -> Task:
        """
        新增任务运行，包含所有字段信息

        Args:
            db: 数据库会话
            task_id: 任务ID
            task_E_id: 任务执行ID
            status: 任务状态，默认为"pending"

        Returns:
            创建的任务对象
        """
        db = self.db
        db_task = Task(
            task_id=task_id,
            task_E_id=task_E_id,
            status=status
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    def update_task_status_by_task_E_id(self, task_E_id: str, status: str) -> Optional[Task]:
        """
        根据task_E_id更新任务实例状态

        Args:
            db: 数据库会话
            task_E_id: 任务执行ID
            status: 新的状态

        Returns:
            更新后的任务对象或None
        """
        db = self.db
        db_task = db.query(Task).filter(Task.task_E_id == task_E_id).first()
        if db_task:
            db_task.status = status
            db.commit()
            db.refresh(db_task)
        return db_task

    def get_task_status_by_task_E_id(self, task_E_id: str) -> Optional[str]:
        """
        根据task_E_id查询任务实例状态

        Args:
            db: 数据库会话
            task_E_id: 任务执行ID

        Returns:
            任务状态或None
        """
        db = self.db
        db_task = db.query(Task).filter(Task.task_E_id == task_E_id).first()
        return db_task.status if db_task else None

    def update_task_finish_time_by_task_E_id(self, task_E_id: str) -> Optional[Task]:
        """
        根据task_E_id更新任务完成时间

        Args:
            db: 数据库会话
            task_E_id: 任务执行ID

        Returns:
            更新后的任务对象或None
        """
        db = self.db
        db_task = db.query(Task).filter(Task.task_E_id == task_E_id).first()
        if db_task:
            db_task.finish_time = None
            db.commit()
            db.refresh(db_task)
        return db_task

    def get_task_info_by_task_E_id(self, task_E_id: str) -> Optional[Task]:
        """
        根据task_E_id查询该任务实例的所有信息

        Args:
            db: 数据库会话
            task_E_id: 任务执行ID

        Returns:
            任务对象或None
        """
        db = self.db
        return db.query(Task).filter(Task.task_E_id == task_E_id).first()