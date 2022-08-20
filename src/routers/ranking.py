from fastapi import APIRouter

from pydantic import BaseModel

from typing import List


class UserInfo(BaseModel):
    name: str
    rank: int
    point: int
    is_me: bool


router = APIRouter()


@router.get("/ranking/{user_id}", response_model=List[UserInfo])
async def get_ranking(user_id: int):
    users = []
    users.append(UserInfo)
    
    return users 
