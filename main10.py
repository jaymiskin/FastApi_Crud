# standard method using this one not ORM method
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

#  This 3 models required for database connection
import psycopg2
import psycopg2.extras 
import time
# https://github.com/attardi/deepnl/issues/54q --- imp link

app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to my api"}

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

                                  # |   
# This Code for database connection V

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin', cursor_factory=psycopg2.extras.RealDictCursor)
        cursor = conn.cursor()
        print("============================== Database connection was succesfull! ==============================")
        break
    except Exception as error:
        print("////////////////////////////////////////// Connecting to database failed //////////////////////////////////////")
        print("Error:", error)
        time.sleep(3)




my_posts = [{"title": "title of post", "content": "content of post", "id": 4},
            {"title": "my fav food burger","content": "i like pizza", "id": 2}, 
            {"title": "my fav song Freeversefet", "content": "i like kr$na", "id": 3},
            {"title": "my fav movie dhool", "content": "i like gaming", "id": 1}
]

@app.post("/createpost", status_code=status.HTTP_201_CREATED, tags=["crud_operation"])
def create_post(newpost: Post):
    # post_dict = newpost.dict()
    # post_dict['id'] = randrange(0, 100000000)
    # my_posts.append(post_dict)
    # my_posts.sort(key=lambda x: x["id"])

    # cursor.execute(f"INSERT INTO posts (title, content, published) VALUES ({newpost.title},{newpost.content},{newpost.published})")
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,(newpost.title, newpost.content, newpost.published))
    db_post = cursor.fetchone()
    conn.commit()
    return {"data_added": db_post}


@app.get("/posts", tags=["crud_operation"])
def get_post():
    my_posts.sort(key=lambda x: x["id"])
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    return {"my_data_db": posts}



@app.get("/posts/{id}", tags=["crud_operation"])
def get_posts(id: int, response: Response):
    cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    print(post)

    # post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    return {"post_details": post}


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["crud_operation"])
def delete_post(id: int):
    # deleting post
    # find the index in the arraythat has required ID
    # my_posts.pop(index)

    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    delete_post = cursor.fetchone()
    # index = find_index_post(id)
    conn.commit()

    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    # my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", tags=["crud_operation"])
def update_post(id: int, post: Post):
    # index = find_index_post(id)

    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title,post.content,post.published,str(id),))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[index] = post_dict
    return {'data_updated' : updated_post}  