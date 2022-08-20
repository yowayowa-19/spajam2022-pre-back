from fastapi import APIRouter

router = APIRouter()


@router.get("/ranking")
async def get_ranking():
    return
