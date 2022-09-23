import logging
import os

from mongoengine import connect
from mongoengine.fields import ObjectIdField
from pydantic.error_wrappers import ValidationError


class MongoDatabase:
    @classmethod
    async def connect(cls):
        try:
            connect(
                db=os.getenv("MONGO_NAME"),
                host=os.getenv("MONGO_HOST"),
                port=int(os.getenv("MONGO_PORT")),
                username=os.getenv("MONGO_USERNAME"),
                password=os.getenv("MONGO_PASSWORD"),
                authentication_source=os.getenv("MONGO_AUTH")
            )
            logging.info("Connection established to mongo database")
        except ValidationError as validation_error:
            logging.exception("Invalid Cosmo url", exc_info=validation_error)


class MongoengineBaseModel:
    id_ = ObjectIdField(binary=False, primary_key=True)

    meta = {
        "collection": lambda coll: coll.__name__.removesuffix(
            "Mongoengine"
        ).lower()
    }
