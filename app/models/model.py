from pydantic import BaseModel, Field, EmailStr
from .PyObjectId import PyObjectId
from bson import ObjectId


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some title about animals",
                "content": "Some content about animals"
            }

        }


class PostForPostSchema(BaseModel):
    title: str = Field(default=None)
    content: str = Field(default=None)


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Quyen",
                "email": "quyenld@gmail.com",
                "password": "123134"
            }
        }


class UserGetingSchema(UserSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "demo": {
                "email": "quyenld@gmail.com",
                "password": "123134"
            }
        }
