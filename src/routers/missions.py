from fastapi import APIRouter

from pydantic import BaseModel

from typing import List


class Mission(BaseModel):
    mission_id: int
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
    mission = {
            "mission_id": 1,
            "title": "sample mission",
            "describe": "ganbatte",
            "point": 10,
            "status": False
            }
    missions = {
            "weekly": [mission],
            "daily": [mission]
            }
    return missions


@router.post("/missions/{user_id}/done/mission_id{}")
async def done_mission(user_id: int, mission_id: int):
    return {"status": True}
