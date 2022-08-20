from fastapi import APIRouter

from types import Credential, User


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=Credential)
async def get_user(user_id: int):
    """ユーザー情報取ってくる"""
    # ユーザー情報をDBから取ってくる
    credential = Credential
    credential.email = "sample"

    return credential


@router.post("/register", response_model=Credential)
async def register_user(credential: Credential):
    """ユーザー新規登録"""
    # ユーザーの登録処理
    return credential


@router.post("login")
async def login_user():
    pass


@router.post("/profile", response_model=User)
async def update_profile(user: User):
    """ユーザーの情報更新"""
    return User
