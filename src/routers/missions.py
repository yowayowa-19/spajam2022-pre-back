from fastapi import APIRouter
from pydantic import BaseModel
from repository import db


class Mission(BaseModel):
    mission_id: int
    title: str
    describe: str
    point: int
    current_point: int
    status: bool


class Missions(BaseModel):
    weekly: list[Mission]
    daily: list[Mission]


class DoneMission(BaseModel):
    user_id: int
    mission_id: int
    type: str # daily | weekly
    point: int


router = APIRouter()


@router.get("/missions", response_model=Missions)
async def get_missions(user_id: int):
    # mission = {
    #     "mission_id": 1,
    #     "title": "sample mission",
    #     "describe": "ganbatte",
    #     "point": 10,
    #     "status": False,
    # }

    daily = db.get_missions(user_id, "daily")
    weekly = db.get_missions(user_id, "weekly")

    missions = {"daily": daily, "weekly": weekly}

    return missions


@router.post("/mission", response_model=DoneMission)
async def done_mission(done_mission: DoneMission):
    # update_task()
    return {"status": True}


# ほんとは叩ける先を絞る必要がある
@router.get("/create/missions/")
async def create_missions(type: str):
    if type == "daily" or type == "weekly":
        db.create_missions(type)
        return {"status": True}
    else:
        return {"status": False}


# ほんとは叩ける先を絞る必要がある
@router.delete("/missions")
async def delete_missions(type: str):
    if type == "daily" or type == "weekly":
        return {"status": True}    
    else:
        return {"status": False}
