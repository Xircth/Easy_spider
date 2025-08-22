import json

config_path = "config.json"
mysql_config_path = "./execute/mysql_config.json"

def config_init():
    with open(config_path, 'r', encoding="utf-8") as f:
        configs = json.load(f)
        # print(configs["mysql_config"])
    with open(mysql_config_path,"w",encoding="utf-8") as f:
        f.write(json.dumps(configs["mysql_config"]))
    pass

def get_config(key:str):
    with open(config_path,"r",encoding="utf-8") as f:
        configs = json.load(f)
    try:
        return configs[key]
    except Exception as e:
        return None


if __name__ == "__main__":
    config_init()