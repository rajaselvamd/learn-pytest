from fastapi import FastAPI
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2},
]

def find_post(id):
    fp = {}
    for p in my_posts:
        print(p['id'])
        if p['id'] == id:
            fp = p
            break
    if fp:
        return fp
    return None

@app.get("/")
def root():
    return {"message": "Hello World, Welcome to my API!!!"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']}, content: {payload['content']} "}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id):
    post = find_post(id)
    print(post)
    if post:
        return {"post_detail": f"here is post {id}"}
    else:
        return {"post_detail": f"id {id} is not found"}
