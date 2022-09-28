from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField, UUIDField, DateTimeField, IntField,
    EmbeddedDocumentField
)

from src.infra.mongoengine.mongoengine import MongoengineBaseModel


class UsersMongoengine(EmbeddedDocument):
    rfid = UUIDField()
    name = StringField()
    credits = IntField()
    created_at = DateTimeField()
    valid_until = DateTimeField()


class AttendanceMongoengine(Document, MongoengineBaseModel):
    user_id = EmbeddedDocumentField(UsersMongoengine)
    clock_in = DateTimeField()
