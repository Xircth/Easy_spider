from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from typing import Any, Optional

class ApiResponse:
    @staticmethod
    def success(data: Any = None, message: str = "Success", code: int = 200) -> JSONResponse:
        content = {
            "code": code,
            "message": message,
            "data": data
        }
        return JSONResponse(content=content, status_code=200)

    @staticmethod
    def error(message: str = "Error", code: int = 400, status_code: int = 200) -> JSONResponse:
        content = {
            "code": code,
            "message": message,
            "data": None
        }
        return JSONResponse(content=content, status_code=status_code)