from fastapi import APIRouter


from repository.db import create_user
from pydantic import BaseModel


class Credential(BaseModel):
    email: str
    user_name: str
    password: str


class User(BaseModel):
    user_id: int
    region: str
    has_vehicles: bool
    has_aircon: bool
    has_tv: bool
    annotation: str


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """ユーザー情報取ってくる"""
    # ユーザー情報をDBから取ってくる
    user = {
            "user_id": 2000,
            "region": "japan",
            "has_vehicles": True,
            "has_aircon": False,
            "has_tv": False,
            "annotation": "mock"
            }

    return user
    # return credential


@router.post("/register")
async def register_user(credential: Credential):
    """
    ユーザー新規登録
    credentialを受け取って、ユーザー登録を行う
    成功時: 200
    失敗時: 400
    """
    result = create_user(credential)
    if result:
        return 
    # error


@router.post("/login")
async def login_user(credential: Credential):
    """
    ログイン
    credentialを受け取って、ログインを行う
    user_id: intを返す
    login後のAPI呼び出し時にuser_idパラメータで与える必要あり
    成功時: user_id > 1
    失敗時: 0
    """
    return {"user_id": 2000}


@router.post("/profile", response_model=User)
async def update_profile(user: User):
    """
    ユーザーの情報更新
    Userを受け取って、profileの更新を行う
    登録したUserをそのまま帰す
    """
    return User
