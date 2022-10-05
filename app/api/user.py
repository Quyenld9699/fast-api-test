from fastapi import APIRouter, Body
from app.auth.jwt_handler import signJWT
from app.constant.data import users
from app.models.model import UserLoginSchema, UserSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# normal funtion


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# User sign up


@router.post("/sign-up")
def user_sign_up(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


@router.post("/login")
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details"
        }
