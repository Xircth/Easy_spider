import jwt as pyjwt
from datetime import datetime, timedelta
from typing import Dict, Any
from fastapi import HTTPException, status
from app.utils.config_init import get_config

# 获取JWT配置
jwt_config = get_config("jwt_config") or {
    "secret_key": "your-super-secret-key-change-in-production",
    "algorithm": "HS256",
    "access_token_expire_minutes": 3000000
}

SECRET_KEY = jwt_config["secret_key"]
ALGORITHM = jwt_config["algorithm"]
ACCESS_TOKEN_EXPIRE_MINUTES = jwt_config["access_token_expire_minutes"]

def create_access_token(data: Dict[str, Any], expires_delta: timedelta = None) -> str:
    """
    创建JWT访问令牌
    
    Args:
        data: 要编码到token中的数据
        expires_delta: token过期时间
        
    Returns:
        编码后的JWT token字符串
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = pyjwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str) -> Dict[str, Any]:
    """
    验证JWT访问令牌
    
    Args:
        token: 要验证的token
        
    Returns:
        解码后的token数据
        
    Raises:
        HTTPException: 当token无效或过期时抛出
    """
    try:
        payload = pyjwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except pyjwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token已过期",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except pyjwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的Token",
            headers={"WWW-Authenticate": "Bearer"},
        )