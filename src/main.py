from fastapi import APIRouter

router = APIRouter()


@router.put("/link")
async def add_link(link: str):
    