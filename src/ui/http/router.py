import os

from fastapi import APIRouter

from schemas.mongoengine.ru_model import UsersMongoengine

router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", ""))


@router.post("/")
async def test_insert_database(test: str):
    pass
