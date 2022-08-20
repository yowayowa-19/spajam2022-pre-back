from fastapi import APIRouter

from pydantic import BaseModel

from typing import List, Union


class Mission(BaseModel):
    title: str
    describe: str
    point: int
    status: bool


class Missions(BaseModel):
    weekly: List[Mission]
    daily: List[Mission]


router = APIRouter()


@router.get("/missions/{user_id}", response_model=Missions)
async def get_missions(user_id: int):
    missions = Missions
    return missions
