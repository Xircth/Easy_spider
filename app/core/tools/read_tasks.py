import os
import json
import tailer

def read_tasks():
    """
    读取execute/tasks/目录下所有json文件，提取id、name、url、update_time字段
    返回列表字典格式
    """
    # 构建tasks目录路径
    tasks_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'execute', 'tasks')
    tasks_dir = os.path.abspath(tasks_dir)
    
    tasks_list = []
    
    # 遍历tasks目录下的所有文件
    for filename in os.listdir(tasks_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(tasks_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    task_data = json.load(f)
                    
                    # 提取需要的字段
                    task_info = {
                        'id': task_data.get('id'),
                        'name': task_data.get('name'),
                        'url': task_data.get('url'),
                        'update_time': task_data.get('update_time')
                    }
                    tasks_list.append(task_info)
            except Exception as e:
                print(f"读取文件 {filename} 时出错: {e}")
                continue
    
    return tasks_list

def _get_task_by_id(id):
    tasks_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'execute', 'tasks')
    tasks_dir = os.path.abspath(tasks_dir)
    task_dir = tasks_dir + '\\' + str(id) + '.json'
    try:
        with open(task_dir, 'r', encoding='utf-8') as f:
            task_data = json.load(f)
            task_info = {
                'id': task_data.get('id'),
                'name': task_data.get('name'),
                'url': task_data.get('url'),
                'update_time': task_data.get('update_time'),
                'output_format':task_data.get('outputFormat'),
                'save_name':task_data.get('saveName'),
                'remove_duplicate':task_data.get('removeDuplicate'),
                "create_time": task_data.get('create_time'),
                "update_time": task_data.get('update_time')
            }
            return task_info
    except Exception as e:
        print(f"读取文件 {task_dir} 时出错: {e}")
                    
def read_logs(id,last_n,save_name):
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '..', 'execute', 'Data')
    logs_dir = os.path.abspath(logs_dir)
    log_dir = logs_dir + '\\' + "Task_" + str(id) + '\\' + save_name +'.log'
    try:
        with open(log_dir,'r', encoding='utf-8',errors='replace') as f:
            lines = tailer.tail(f,last_n)
            return lines
    except Exception as e:
        print(f"读取文件 {log_dir} 时出错: {e}")
    

# 如果需要直接运行测试
if __name__ == "__main__":
    for i in read_logs(1,50,"bilibili_test"):
        print(i)