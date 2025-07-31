
from fastapi import FastAPI, status         
from pydantic import BaseModel              
from typing import List                     


app = FastAPI()


class Post(BaseModel):
    author: int    
    title: str      
    content: str
    creation_datetime: int


posts_list: List[Post] = []


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def add_players(new_posts: List[Post]):
    posts_list.extend(new_posts)     
                 


@app.get("/posts", status_code=status.HTTP_200_OK)
async def get_posts():
    return posts_list

