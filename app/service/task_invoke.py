import threading
import time
import uuid
from app.service.task_service import TaskService
from app.core.tools.command_calling import generate_command,summon_subprocess
import sys

taskService = None

class Task:
    def __init__(self,task_id:str,task_E_id:str):
        self.task_id = task_id    # 为任务id
        self.task_E_id = task_E_id    # 为运行时线程分配id
        self.status = "pending"
        self.created_time = time.time()
        
    
    def run(self,task_id,E_id,platform):
        win64_path = "execute/chrome_win64/easyspider_executestage.exe"
        linux64_path = "execute/chrome_linux64/easyspider_executestage"
        if platform == "win":
            cmd = generate_command(win64_path, 
                            [task_id], 
                            0, 
                            "http://localhost:8074", 
                            "H:/work/Easy_spider_reborn/execute/", 
                            1, 
                            "local", 
                            "config.json", 
                            "")
        elif platform == "linux":
            cmd = generate_command(linux64_path, 
                            [task_id], 
                            0, 
                            "http://localhost:8074", 
                            "H:/work/Easy_spider_reborn/execute/", 
                            1, 
                            "local", 
                            "config.json", 
                            "")
        taskService.update_task_status_by_task_E_id(task_E_id=E_id,status="running")
        summon_subprocess(cmd)
        taskService.update_task_status_by_task_E_id(task_E_id=E_id,status="finished")
        taskService.update_task_finish_time_by_task_E_id(E_id)
        
    

class TaskManager:
    def __init__(self):
        self.debug = False
        if not self.debug:
            from app.database import get_db
            from sqlalchemy.orm import Session
            self.db = next(get_db())
            global taskService
            if taskService is None:
                taskService = TaskService(db=self.db)
            else:
                taskService.db = self.db
        self.tasks = {}
    
    def create_task(self,task_id:str): # 以任务id创建一个任务运行实例（线程）返回一个EID
        task_E_id = str(uuid.uuid4())[:8]
        self.tasks[task_E_id] = Task(task_id,task_E_id)
        if not self.debug:
            taskService.create_task(task_id=task_id,task_E_id=task_E_id)
        return self.tasks[task_E_id]
    
    def get_task_by_E_id(self,task_E_id:str):
        return self.tasks[task_E_id]
    
    def run_task(self,task_E_id:str): # 运行任务
        self.tasks[task_E_id].run()
        self.tasks[task_E_id].status = "running"
        if not self.debug:
            taskService.update_task_status_by_task_E_id(task_E_id,"running")
    
    def stop_task(self,task_E_id:str): # 停止任务
        self.tasks[task_E_id].status = "stopped"
        del self.tasks[task_E_id]
        if not self.debug:
            taskService.update_task_status_by_task_E_id(task_E_id,"stopped")
            taskService.update_task_finish_time_by_task_E_id(task_E_id)
    
    def get_task_status(self,task_E_id:str): # 获取任务状态
        return self.tasks[task_E_id].status
    
    def get_task_result(self,task_E_id:str): # 获取任务结果
        pass
    
taskManager = TaskManager()
def start_task(task_id):
    task = taskManager.create_task(task_id = task_id)
    print("任务",task_id,"已创建,运行id:",task.task_E_id)
    platform = ""
    if sys.platform == 'linux':
        platform = "linux"
    else:
        platform = "win64"
    
    
    
    thread = threading.Thread(target=task.run,args=(task_id,task.task_E_id,platform,),daemon=True)
    thread.start()
    return task.task_E_id



if __name__ == "__main__":
    start_task(1)
    