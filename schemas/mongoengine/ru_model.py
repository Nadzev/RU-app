from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField, UUIDField, DateTimeField, IntField,
    EmbeddedDocumentField
)

from schemas.pydantic.ru_model_pydantic import Attendance, User
from src.infra.mongoengine.mongoengine import MongoengineBaseModel


class UsersMongoengine(EmbeddedDocument):
    # TODO: mudar rfid para int
    rfid = IntField()
    name = StringField()
    credits = IntField()
    created_at = DateTimeField()

    @classmethod
    def from_entity(cls, user: User):
        return UsersMongoengine(
            rfid=user.rfid,
            name=user.name,
            credits=user.credits,
            created_at=user.created_at
        )


class AttendanceMongoengine(Document, MongoengineBaseModel):
    user = EmbeddedDocumentField(UsersMongoengine)
    clock_in = DateTimeField()

    @classmethod
    def from_entity(cls, attendance: Attendance):
        user_db = UsersMongoengine.from_entity(attendance.user)
        return AttendanceMongoengine(
            id_=attendance.id, user=user_db,
            clock_in=attendance.clock_in
        )
