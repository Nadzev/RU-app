import asyncio

from bson import ObjectId

from datetime import datetime

from schemas.mongoengine.ru_model import AttendanceMongoengine
from schemas.pydantic.ru_model_pydantic import Attendance, User
from src.infra.mongoengine.mongoengine import MongoDatabase


async def funciona():
    await MongoDatabase.connect()
    user = User(
        rfid=19347947958,
        name="testGamer",
        credits=30,
        created_at=datetime.utcnow()
    )
    attendance = Attendance(
        id=ObjectId(), user=user, clock_in=datetime.utcnow()
    )

    attendance_db = AttendanceMongoengine.from_entity(attendance)
    attendance_db.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(funciona())
loop.run_forever()
