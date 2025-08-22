import redis
from typing import Optional
from app.utils.config_init import get_config

# 获取Redis配置
redis_config = get_config("redis_config") or {
    "host": "127.0.0.1",
    "port": 6379,
    "db": 0,
    "password": None,
    "log_pre": "spider:log:",
    "log_TTL": 120,
    "msg_pre": "spider:msg:",
    "msg_TTL": 180
}

# 创建Redis连接
r = redis.Redis(
    host=redis_config["host"],
    port=redis_config["port"],
    db=redis_config["db"],
    # password=redis_config["password"],
    decode_responses=True  # 自动解码响应为字符串
)

def set_verification_code(uuid: str, code: str, expire: int = None) -> bool:
    """
    设置验证码
    
    Args:
        uuid: 用户唯一标识
        code: 验证码
        expire: 过期时间（秒），默认使用配置中的msg_TTL
        
    Returns:
        是否设置成功
    """
    try:
        ttl = expire or redis_config["msg_TTL"]
        key = f"{redis_config['msg_pre']}{uuid}"
        r.setex(key, ttl, code)
        return True
    except Exception as e:
        print(f"设置验证码失败: {e}")
        return False

def get_verification_code(uuid: str) -> Optional[str]:
    """
    获取验证码
    
    Args:
        uuid: 用户唯一标识
        
    Returns:
        验证码字符串，如果不存在则返回None
    """
    try:
        key = f"{redis_config['msg_pre']}{uuid}"
        return r.get(key)
    except Exception as e:
        print(f"获取验证码失败: {e}")
        return None

def delete_verification_code(uuid: str) -> bool:
    """
    删除验证码
    
    Args:
        uuid: 用户唯一标识
        
    Returns:
        是否删除成功
    """
    try:
        key = f"{redis_config['msg_pre']}{uuid}"
        r.delete(key)
        return True
    except Exception as e:
        print(f"删除验证码失败: {e}")
        return False