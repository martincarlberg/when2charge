from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ShouldICharge/")
def read_item(item: int):
    return {"Answer":"Yes, charging is good"}
