import os

from fastapi import APIRouter

router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", ""))
