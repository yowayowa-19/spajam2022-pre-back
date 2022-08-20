from fastapi import APIRouter

from types import Credential, User

from repository.db import create_user


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}")
async def get_user(user_id: int):
    """ユーザー情報取ってくる"""
    # ユーザー情報をDBから取ってくる
    credential = Credential
    credential.email = "sample"
    return {"id": 1}
    # return credential


@router.post("/register", response_model=Credential)
async def register_user(credential: Credential):
    """ユーザー新規登録"""
    # ユーザーの登録処理

    result = create_user(credential)
    if result:
        return {"id": result}
    # error


@router.post("login")
async def login_user():
    pass


@router.post("/profile", response_model=User)
async def update_profile(user: User):
    """ユーザーの情報更新"""
    return User
