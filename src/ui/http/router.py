import os

from fastapi import APIRouter

router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", ""))


@router.post("/")
async def test_insert_database(test: str):
    pass
