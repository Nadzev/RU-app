import logging
import os

from mongoengine import connect
from pydantic.error_wrappers import ValidationError
from pydantic.main import BaseModel
from pydantic.networks import AnyUrl


class MongoConnectionConfig(BaseModel):
    host: AnyUrl


class MongoDatabase:
    @classmethod
    async def connect(cls):
        try:
            config_connection = MongoConnectionConfig(
                host=os.getenv("MONGO_URL")
            )
            connect(**config_connection.dict())
            logging.info(
                "Connection established to mongo database in host %s",
                config_connection.host.host
            )
        except ValidationError as validation_error:
            logging.exception("Invalid Cosmo url", exc_info=validation_error)
