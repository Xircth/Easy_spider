from fastapi import FastAPI

app = FastAPI(title="Pulgin_Project", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
