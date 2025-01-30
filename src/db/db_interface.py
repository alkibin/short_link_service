from abc import ABC, abstractmethod


class AbstractDb(ABC):
    @abstractmethod
    async def new_record(self, record):
        ...

    @abstractmethod
    async def find_record(self, record):
        ...