log_path = "./execute/Data"
# 读取任务的日志最后n行
def log_reader(E_id,last_n,task_name):
    task_log_path = log_path + "/Task_" + str(E_id) + "/" + task_name +".log"
    with open(task_log_path,"r" ,encoding="utf-8") as f:
        lines = f.readlines()
        return lines[-last_n:]
    
if __name__ == "__main__":
    for i in log_reader(1,100,"bilibili_test"):
        print(i)
    pass