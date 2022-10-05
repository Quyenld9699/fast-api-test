from fastapi import APIRouter, Depends, HTTPException
from app.auth.jwt_bearer import jwtBearer
from app.models.model import PostForPostSchema, PostSchema
from app.constant.data import posts

router = APIRouter(
    prefix="/postes",
    tags=["postes"],
    dependencies=[Depends(jwtBearer())],   # => toàn bộ api ở page này đều phải authen
    responses={404: {"description": "Not found"}},
)

# Get - all
@router.get("/" )
def get_posts():
    return {
        "data": posts
    }

# Get single post by (id)
@router.get("/{id}" )
def get_one_post(id: int):
    if id > len(posts):
        return {
            "error": "Post with this id not exist."
        }
    
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

@router.post("/")
def add_post(post: PostForPostSchema):
    new_id = len(posts) + 1
    new_post = PostSchema(id=new_id, content=post.content, title=post.title)
    posts.append(new_post.dict())
    return {
        "info": "success added",
        "post": new_post
    }
