from fastapi import FastAPI
from src.infra.mongoengine.mongoengine import MongoDatabase
from src.ui.http.router import router
from src.mqtt_service.mqtt import Mqtt
mqtt = Mqtt(client_id='ru-app')
mqtt.main()
app = FastAPI()
app.include_router(router)
app.add_event_handler("startup", MongoDatabase.connect)

    