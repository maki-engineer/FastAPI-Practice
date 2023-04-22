from enum import Enum
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet  = "resnet"
  lenet   = "lenet"

class Item(BaseModel):
  name: str
  description: Union[str, None] = None
  price: float
  tax: Union[float, None] = None

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
def root():
  return {"message": "Hello, World."}

@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
  return fake_items_db[skip : skip + limit]

@app.post("/items")
async def create_item(item: Item):
  item_dict = item.dict()
  if item.tax:
    price_with_tax = item.price + item.tax
    item_dict.update({"price_with_tax": price_with_tax})
  return item_dict

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None, short: bool = False):
  item = {"item_id": item_id}
  if q:
    item.update({"q": q})
  if not short:
    item.update({"description": "This is an amazing item that has a long descriptioin."})
  return item

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
  return {"item_id": item_id, **item.dict()}

@app.get("/users/me")
def read_user_me():
  return {"user_id": "the current user."}

@app.get("/users/{user_id}")
def read_user(user_id: int):
  return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTW!"}

  if model_name.value == "lenet":
    return {"model_name": model_name, "message": "LeCNN all the images"}

  return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
  return {"file_path": file_path}