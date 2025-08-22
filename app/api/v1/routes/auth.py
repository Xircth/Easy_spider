from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import HTTPAuthorizationCredentials
from typing import Dict
import random
import string
import base64
from io import BytesIO
from captcha.image import ImageCaptcha
from sqlalchemy.orm import Session
from app.utils.result import ApiResponse
from app.database import get_db
from app.service.user_service import UserService
from app.utils.jwt_util import create_access_token
from app.utils.redis_tool import set_verification_code, get_verification_code, delete_verification_code

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


def generate_captcha_text(length: int = 6) -> str:
    """
    生成指定长度的验证码文本
    
    Args:
        length: 验证码长度，默认6位
        
    Returns:
        生成的验证码字符串
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@router.get("/captcha")
async def get_captcha():
    """
    获取图形验证码
    
    Returns:
        包含图形验证码base64编码和UUID的响应
    """
    # 生成UUID
    import uuid
    captcha_uuid = str(uuid.uuid4())
    
    # 生成验证码文本
    captcha_text = generate_captcha_text()
    
    # 使用captcha库生成图形验证码
    image = ImageCaptcha(width=120, height=40)
    image_bytes = image.generate(captcha_text).getvalue()
    
    # 将图片转换为base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    
    # 使用UUID作为键存储验证码到Redis
    if set_verification_code(captcha_uuid, captcha_text):
        return ApiResponse.success(
            data={
                "image": f"data:image/png;base64,{image_base64}",
                "uuid": captcha_uuid
            },
            message="获取验证码成功"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="验证码生成失败"
        )

@router.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    """
    用户登录
    
    Args:
        request: HTTP请求对象
        db: 数据库会话
        
    Returns:
        登录结果，包含access-token
        
    Raises:
        HTTPException: 当请求数据不完整或验证失败时抛出相应错误
    """
    # 解析JSON请求体
    try:
        body = await request.json()
        uuid = body.get("uuid")
        captcha = body.get("captcha")
        username = body.get("username")
        password = body.get("password")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="请求体格式错误，必须为有效的JSON"
        )
    
    # 验证所有必需字段
    if not all([uuid, captcha, username, password]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="所有字段均不能为空"
        )
    
    # 验证验证码
    print("验证验证码")
    stored_captcha = get_verification_code(uuid)
    if not stored_captcha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="验证码已过期"
        )
    
    if stored_captcha != captcha:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="验证码错误"
        )
    
    # 验证用户是否存在
    print("查询用户")
    user = UserService.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户不存在"
        )
    
    # 验证密码
    import hashlib
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    hashed_password = md5.hexdigest()
    
    if user.hashed_password != hashed_password:
        print("user:",user.hashed_password)
        print("input:",hashed_password)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="密码错误"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户已被禁用"
        )
    
    # 生成JWT token
    access_token_expires = None  # 使用默认过期时间
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id}
    )
    
    # 删除已使用的验证码
    delete_verification_code(uuid)
    
    return ApiResponse.success(
        data={
            "access-token": access_token,
            "token_type": "bearer",
            "username": user.username,
            "user_id": user.id
        },
        message="登录成功"
    )
    
    