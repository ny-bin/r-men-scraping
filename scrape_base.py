from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
from os import link


class Scrape_Base(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    async def scrape_restaurant(self):
        pass


class Restaurant():
    def __init__(
            self,
            restaurant_name: str,
            phone_number: int,
            address: str,
            prefecture_id: int,
            description: str,
            link_url: str
    ) -> None:
        self.restaurant_name: str = restaurant_name
        self.phone_number: int = phone_number
        self.address: str = address
        self.prefecture_id: int = prefecture_id
        self.description: str = description
        self.link_url: str = link_url


class Category():
    def __init__(
        self,
        category_list: list[int]
    ):
        self.category_list = category_list
