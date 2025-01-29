from urllib.parse import urlparse
from src.schemas.schemas import Link, AddReturnString
from src.interfaces.bd_interface import AbstractDb
from string import ascii_lowercase
import random


class LinkService:
    def __init__(self, link, db_session):
        self.link = link
        self.db: AbstractDb = db_session

    def parse_link(self):
        return Link(**urlparse(self.link)._asdict())

    def create_return_string(self, parsed_link):
        string = self._shuffle_string(ascii_lowercase)
        return f'{parsed_link.netloc}/{}

    def _shuffle_string(self, string):
        to_list = list(string)
        res = random.sample(to_list, 5)
        return ''.join(res)

    async def check_exists(self, parsed_link):
        pass


    async def save_data(self, prepared_link: Link):
        self.db.save_data(prepared_link)


service = LinkService(link='http://supersite.com/superpage/1/sdropehiu0e9043f', db_session='dfgd')
print(service.parse_link())
