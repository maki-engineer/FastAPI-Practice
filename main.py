from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet  = "resnet"
  lenet   = "lenet"

app = FastAPI()

@app.get("/")
def root():
  return {"message": "Hello, World."}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}

@app.get("/users/me")
def read_user_me():
  return {"user_id": "the current user."}

@app.get("/users/{user_id}")
def read_user(user_id: int):
  return {"user_id": user_id}