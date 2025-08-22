from fastapi import Request, HTTPException, status,Depends
from fastapi.security import HTTPBearer
from typing import Optional
from app.utils.jwt_util import verify_access_token

class JWTBearer(HTTPBearer):
    """
    JWT认证Bearer方案
    用于验证access-token
    """
    
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request) -> Optional[str]:
        """
        验证请求中的access-token
        
        Args:
            request: FastAPI请求对象
            
        Returns:
            验证通过的token字符串
            
        Raises:
            HTTPException: 当token验证失败时抛出
        """
        # 从header中获取access-token
        token = request.headers.get("access-token")
        
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="缺少认证token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # 验证token
        try:
            payload = verify_access_token(token)
            return token
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="无效的认证token",
                headers={"WWW-Authenticate": "Bearer"},
            )

def get_current_user(token: str = Depends(JWTBearer())):
    """
    获取当前登录用户
    作为依赖注入使用
    
    Args:
        token: 经过验证的token
        
    Returns:
        解码后的token payload
    """
    return verify_access_token(token)