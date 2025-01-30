import hashlib
from urllib.parse import urlparse, urlunparse

from fastapi import Depends

from src.db.db_interface import AbstractDb
from src.db.mongo import get_mongo
from src.models.models import Link


class LinkService:
    def __init__(self, db):
        self.db: AbstractDb = db

    async def process_link(self, link):
        link_model = self._parse_link(link)
        short_code = self.create_short_code(link_model, link)

        record = await self.find_record(short_code)
        if record:
            return record.short_code

        link_model.short_code = short_code
        await self.save_data(link_model)
        return short_code

    async def get_long_link(self, short_link):
        link_record = await self.find_record(short_link)
        if link_record:
            return urlunparse((
                link_record.scheme,
                link_record.netloc,
                link_record.path,
                link_record.params,
                link_record.query,
                link_record.fragment
                ))

        return None

    def _parse_link(self, link):
        return Link(**urlparse(link)._asdict())

    def create_short_code(self, link_model, parsed_link):
        string = self._create_md5_hash(parsed_link)
        return f'{link_model.netloc}-{string}'

    def _create_md5_hash(self, input_data, length=5):
        md5_hash = hashlib.md5(input_data.encode()).hexdigest()
        return md5_hash[: len(md5_hash) % length]

    async def find_record(self, parsed_link):
        return await self.db.find_record(parsed_link)

    async def save_data(self, prepared_link: Link):
        await self.db.new_record(prepared_link)


def get_link_service(db=Depends(get_mongo)):
    return LinkService(db)