
from fastapi import FastAPI, status 
from pydantic import BaseModel              
from typing import List                     


app = FastAPI()


class Posts(BaseModel):
    author: int    
    title: str      
    content: str
    creation_datetime: int

posts: List[Posts] = []

@app.post("/posts", status_code=status.HTTP_201_CREATED)  
async def add_posts(new_posts: List[Posts]):

    posts.extend(new_posts)


    return posts




