from bson import ObjectId

from mongoengine import Document
from mongoengine.fields import (
    StringField, ComplexDateTimeField, UUIDField, DateTimeField, IntField
)

from src.infra.mongoengine.mongoengine import MongoengineBaseModel


class AttendanceMongoengine(Document, MongoengineBaseModel):
    user_id = UUIDField()
    clock_in = ComplexDateTimeField()


class UsersMongoengine(Document, MongoengineBaseModel):
    rfid = UUIDField()
    name = StringField()
    balance = IntField()
    created_at = DateTimeField()
