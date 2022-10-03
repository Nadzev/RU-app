from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class User(BaseModel):
    rfid: int
    name: str
    credits: int
    created_at: datetime


class Attendance(BaseModel):
    id: PydanticObjectId
    user: User
    clock_in: datetime
