from array import array
from fastapi import APIRouter, Body
from app.auth.jwt_handler import signJWT
from app.constant.data import users
from app.models.model import UserLoginSchema, UserSchema
from database.index import db
from bson import ObjectId

UserCollection = db.user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# normal funtion


def check_user(data: UserLoginSchema):
    user = UserCollection.find_one({"email": data.email, "password": data.password})
    if user:
        # print(user)
        return True
    return False

# User sign up


@router.post("/sign-up")
def user_sign_up(user: UserSchema = Body(default=None)):
    UserCollection.insert_one(user.dict())
    return signJWT(user.email)


@router.post("/login")
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details"
        }


@router.post("/list-all", response_model=list[UserSchema])
async def get_list_user():
    dataCollection = UserCollection.find({})
    result = []
    for item in dataCollection:
        result.append({"id": str(item["_id"]), **(UserSchema(**item).dict())})

    return result
