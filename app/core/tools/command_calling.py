import subprocess
import json

# 示例指令：
#chrome_win64/easyspider_executestage.exe --ids [12] 
# --user_data 0 
# --server_address http://localhost:8074 
# --config_folder "H:/work/Easy_spide_reborn/execute/" 
# --headless 1 
# --read_type local 
# --config_file_name config.json 
# --saved_file_name 
#chrome_win64/easyspider_executestage.exe --ids [12] --user_data 0 --server_address http://localhost:8074 --config_folder "H:/work/Easy_spider_reborn/execute/" --headless 1 --read_type local --config_file_name config.json --saved_file_name 
#chrome_win64/easyspider_executestage.exe --ids [12] --user_data 0 --server_address http://localhost:8074 --config_folder "H:/work/Easy_spider_reborn/execute/" --headless 1 --read_type local --config_file_name config.json --saved_file_name
win64_path = "execute/chrome_win64/easyspider_executestage.exe"


def generate_command(execute_path,
                     ids: list,
                     user_data, 
                     server_address, 
                     config_folder, 
                     headless = 0, 
                     read_type = "local",
                     config_file_name = "config.json", 
                     saved_file_name = ""):
# 构建命令参数列表
    cmd = [
        execute_path,
        "--ids", json.dumps(ids),                    
        "--user_data", str(user_data),
        "--server_address", server_address,
        "--config_folder", config_folder,
        "--headless", str(headless),
        "--read_type", read_type,
        "--config_file_name", config_file_name,
        "--saved_file_name", saved_file_name
    ]
    return cmd

# print(generate_command(win64_path, [12], 0, "http://localhost:8074", "H:/work/Easy_spide_reborn/execute/", 1, "local", "config.json", ""))

def summon_subprocess(command):
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    # 使用 communicate() 安全地读取输出，避免管道阻塞导致子进程无法退出
    for line in iter(process.stdout.readline, ''):
        print(line.rstrip())
    process.stdout.close()
    process.wait()
    print("[sys]", "end")

if __name__ == "__main__":
    print(" ".join(generate_command(win64_path, [2], 0, "http://localhost:8074", "H:/work/Easy_spider_reborn/execute/", 1, "local", "config.json", "")))
    summon_subprocess(generate_command(win64_path, [2], 0, "http://localhost:8074", "H:/work/Easy_spider_reborn/execute/", 1, "local", "./config.json", ""))

'''
execute/chrome_win64/easyspider_executestage.exe --ids [2] --user_data 0 --server_address http://localhost:8074 --config_folder H:/work/Easy_spider_reborn/execute/ --headless 1 --read_type local --config_file_name ./config.json --saved_file_name


'''

