from fastapi import FastAPI

from src.infra.mongoengine.mongoengine import MongoDatabase
from src.ui.http.router import router

app = FastAPI()
app.include_router(router)
app.add_event_handler("startup", MongoDatabase.connect)
