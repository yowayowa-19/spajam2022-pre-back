from fastapi import APIRouter

router = APIRouter()


@router.get("/missions/{user_id}")
async def get_missions():
    return 
