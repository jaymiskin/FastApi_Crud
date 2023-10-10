"query parameters and any browser are by default use get(method) and query parameters used get method"


# from fastapi import FastAPI

# app = FastAPI()

# demo_items = [{"itemname": "candy"}, {"itemname": "cotton"}, {"itemname": "dark"}, {"itemname": "chocolate"},{"itemname": "ice"},{"itemname": "ice-creame"},{"itemname": "coffe"},{"itemname": "tea"},{"itemname": "ice-tea"}, {"itemname": "chwingam"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return demo_items[skip : skip + limit]


# required and unrequired used 
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{serial_no}")
# async def demofunction(item_id: str, q:str | None = None):
#     if q:
#         return {"item_id" : item_id, "q": q}
#     return {"item_id": item_id}



# Query parameter type conversion
# You can also declare bool types, and they will be converted:
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/{serial_no}")
# async def read_item(serial_no: int, q: str | None = None, gender: bool = False):
#     item = {"serial_no": serial_no}
#     if q:
#         item.update({"q": q})
#     if not gender:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# Required query parameters
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    print(item)
    return item
