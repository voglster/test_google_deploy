from typing import Union

from fastapi import FastAPI
from app.postgres_test import connect, get_data

app = FastAPI()


@app.get("/db")
def db_ep():
    return connect()


@app.get("/db2")
def db_ep():
    return get_data()


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
