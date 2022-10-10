from fastapi import APIRouter, Body
from app.auth.jwt_handler import signJWT
from app.models.model import UserGetingSchema, UserLoginSchema, UserSchema
from database.index import db
from passlib.context import CryptContext
from bson import ObjectId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


UserCollection = db.user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# normal funtion


def hash_password(password):
    return pwd_context.hash(password)


def check_user(data_post: UserLoginSchema):
    user = UserCollection.find_one({"email": data_post.email})
    # typeof user is dict => dùng biến ở dạng variable[key]
    # object class thì mới truy cập bằng variable.key
    if user and pwd_context.verify(data_post.password, user["password"]):
        return True
    return False

# User sign up


@router.post("/sign-up")
def user_sign_up(user: UserSchema = Body(default=None)):
    UserCollection.insert_one({**user.dict(), "password": hash_password(user.password)})
    return signJWT(user.email)


@router.post("/login")
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details"
        }


@router.post("/list-all", response_model=list[UserGetingSchema])
async def get_list_user():
    dataCollection = UserCollection.find({})
    result = []
    for item in dataCollection:
        # print(item)
        result.append(UserGetingSchema(**item).dict())
        # result.append({"id": str(item["_id"]), **(UserSchema(**item).dict())})

    return result


@router.post("/{id}", response_model=UserGetingSchema)
async def get_user_by_id(id: str):
    dataCollection = UserCollection.find_one({"_id": ObjectId(id)})
    if dataCollection:
        return dataCollection
        # return UserGetingSchema(**dataCollection)
    return {
        "error": "Post with this id not exist."
    }
