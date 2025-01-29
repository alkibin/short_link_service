from abc import ABC, abstractmethod


class AbstractDb(ABC):
    @abstractmethod
    async def save_data(self, data):
        ...

    @abstractmethod
    async def get_data(self, property):
        ...