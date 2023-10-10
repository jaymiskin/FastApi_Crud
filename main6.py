# from fastapi import FastAPI
# from pydantic import BaseModel,Field

# class Item_Base(BaseModel):
#     name: str
#     decscription: str = Field(default=None)
#     price: float
#     bill: float = Field(default=None)


# app = FastAPI()


# @app.post("/items/", tags=["Price"])
# async def create_item(item: Item_Base):
#     print(item)
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# class Item(BaseModel):
#     name: str
#     decscription: str = Field(default=None)
#     address: str
#     price: float
#     tax: float = Field(default=None)

# app = FastAPI()

# @app.post('/items/', tags=['Local'])
# async def function(item: Item):
#     item_dict = item.dict()
#     if item.price:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price with tax": price_with_tax})
#         print(item_dict)
#     return item_dict



from fastapi import FastAPI
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    description: str = Field(default=None)
    price: int
    tax: float = Field(default=None)


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result