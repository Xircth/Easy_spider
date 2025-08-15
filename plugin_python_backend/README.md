# Plugin Python Backend

这是一个基于 FastAPI 的 Python 后端项目。

## 项目结构

```
plugin_python_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── routes/
│   │           ├── __init__.py
│   │           └── test.py
│   ├── core/
│   │   └── exceptions.py
│   ├── main.py
│   └── __init__.py
├── test/
├── requirements.txt
├── README.md
└── activate_env.cmd
```

## API 接口

### GET /

- 描述: 根路径
- 响应: `{"message": "Welcome to FastAPI!"}`

### GET /plugin/test

- 描述: 测试接口
- 响应: `{"message": "Hello World"}`

## 快速开始

1. 创建并激活虚拟环境:
   ```bash
   .\venv\Scripts\activate
   ```

2. 安装依赖:
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用:
   ```bash
   uvicorn app.main:app --reload