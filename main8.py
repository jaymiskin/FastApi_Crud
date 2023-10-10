from fastapi import FastAPI
# from fastapi.params import Bodys
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


@app.get("/")
def root():
    return {"mgs": "Welcome to my api"}


# title str, content str

class Post(BaseModel):
    title: str
    content: str
    discription: str
    published: bool = True
    rating: Optional[int] = None


@app.post("/createpost")
def create_post(newpost: Post):
    print(newpost)
    print(newpost.dict())
    return {"data": newpost}


my_posts = [{"title": "title of post", "content": "content of post", "id": 1},
            {"title": "my fav food burger","content": "i like pizza", "id": 2}, 
            {"title": "my fav song Freeversefet", "content": "i like kr$na", "id": 3},
            {"title": "my fav movie dhool", "content": "i like gaming", "id": 4}
]


@app.get("/posts")
def get_post():
    print(my_posts)
    return {"my_data": my_posts}
