from pymongo import AsyncMongoClient

from src.db.db_interface import AbstractDb
from src.models.models import Link

client = AsyncMongoClient()


class MongoDb(AbstractDb):
    async def new_record(self, data):
        await Link(**data.model_dump()).insert()

    async def find_record(self, record):
        return await Link.find_one(Link.short_code == record)


def get_mongo():
    return MongoDb()
