from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Hello DevOps - FastAPI", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello, DevOps! (FastAPI)"}

@app.get("/hello/{name}")
def read_name(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/greet")
def greet():
    return {"message": "Hello from feature branch!"}
