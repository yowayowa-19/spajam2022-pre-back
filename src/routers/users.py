from fastapi import APIRouter, HTTPException

from repository.db import create_user, password_check_user, update_user_profile, get_user_info
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
    total_point: int
    # annotation: str

    class Config:
        orm_mode = True


class UserInfo(BaseModel):
    user_name: str
    total_points: int


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", response_model = UserInfo)
async def get_user(user_id: int):
    """ユーザー情報取ってくる"""
    # ユーザー情報をDBから取ってくる

    if user_id == 0:
        raise HTTPException(
                status_code=400,
                detail="ERROR: invalid user_id")
    res = get_user_info(user_id)
    return res
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
    if not result:
        raise HTTPException(
                status_code=400,
                detail="ERROR: register\n"
            )
    return {"result": "success"}


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
    result = password_check_user(credential)
    if result == 0:
        raise HTTPException(
                status_code=400,
                detail="ERROR: login\n"
            )
    return {"user_id": result}


@router.post("/profile", response_model=User)
async def update_profile(user: User):
    """
    ユーザーの情報更新
    Userを受け取って、profileの更新を行う
    登録したUserをそのまま帰す
    """
    result = update_user_profile(user)
    return result
