from src.interfaces.bd_interface import AbstractDb
from pymongo import AsyncMongoClient

client = AsyncMongoClient()


class MongoDb(AbstractDb):
    def __init__(self, client):
        self.client = client

    async def save_data(self, data):
