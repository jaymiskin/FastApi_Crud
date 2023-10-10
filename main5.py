# "body parameters are used to body part and any browser are by default use get(method) and body parameters used post method"

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class demo_pro(BaseModel):
    name: str
    age: int
    percentage: float
    address: str
    gender: str

@app.post("/items/")
async def demo(item:demo_pro):
    print(item)
    return demo