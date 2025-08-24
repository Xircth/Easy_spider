from fastapi import APIRouter,Depends
from app.api.v1.routes import task_router, user_router, auth_router,doc_router
from app.core.security import JWTBearer, get_current_user

api_router = APIRouter()
api_router.include_router(task_router,dependencies=[Depends(get_current_user)])
api_router.include_router(user_router,dependencies=[Depends(get_current_user)])
api_router.include_router(doc_router ,dependencies=[Depends(get_current_user)])
api_router.include_router(auth_router)