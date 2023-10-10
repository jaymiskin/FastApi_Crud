from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}




# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: int):
#     return {"user_no": user_id}


@app.get("/users")
async def read_user():
    return ["Rick", "Harry"]


@app.get("/users1")
async def read_user2():
    return ["Bean", "Om"]