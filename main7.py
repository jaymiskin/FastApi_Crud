# Query Parameters and String Validations

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/", tags=["Local"])
# async def myfun(R: str | None = None):
#     results = {"items": [{"item_id": "Lal"}, {"item_no": "20"}]}
#     if R:
#         results.update({"R": R})
#     return results


# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str | None = Query(default=None,max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# from typing import Annotated

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# Add regular expressions
# from typing import Annotated
# from fastapi import FastAPI, Query
# from pydantic import Required



# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=5)] = Required):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results



# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: list[str]  | None = Query(default=None)):
#     query_items = {"items": q}
#     return query_items


# Dropbox amazing
# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/", tags=["Dropbox"])
# async def read_items(q: list[str]  | None = Query(default=["Jay", "Miskin", "Augst", "Always"])):
#     query_items = {"items": q}
#     print(query_items)
#     return query_items



# You can add a title:
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    r: str | None = Query(default=None, title="Query string", min_length=3)
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if r:
        results.update({"items": r})
    return results