

execute_bin_path = ""
platform = "win"


# 参考命令格式:
# chrome_win64/easyspider_executestage.exe --ids [12] --user_data 0 --server_address http://localhost:8074 --config_folder "H:/work/Easy_spider/ElectronJS/" --headless 1 --read_type local --config_file_name config.json --saved_file_name 




if __name__ == "__main__":
    
    if platform == "win":
        execute_bin_path = "chrome_win64\easyspider_executestage.exe"
    elif platform == "linux":
        execute_bin_path = "chrome_linux64\easyspider_executestage"
    else:
        raise ValueError("platform is not supported")
    




