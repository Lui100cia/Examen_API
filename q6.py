from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Post(BaseModel):
    author: int    
    title: str      
    content: str
    creation_datetime: int


posts_list: List[Post] = []

@app.put("/posts")
def add_or_update_post(post: Post):
    
    
    for i, existing_post in enumerate(posts_list):
        if existing_post.title == post.title:
            
            if existing_post != post:
               
                posts_list[i] = post
                return {"message": "Posts updated", "posts": post}
            else:
                
                return {"message": "No changes detected", "post": post}

   
    posts_list.append(post)
    return {"message": "Post added", "posts": post}


@app.get("/posts")
def get_posts():
    return posts_list


