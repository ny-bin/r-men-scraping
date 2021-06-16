from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
import datetime

import db_lib


class Scrape_Base(metaclass=ABCMeta):
    def __init__(self):
        self.con = db_lib.connect()
        pass

    @abstractmethod
    def scrape_restaurant(self):
        pass

    def save_shop_data(self, restaurant: Restaurant):
        # DBへ保存
        sql = f"""insert into shops(name,
                               phone_number,
                               prefecture_id,
                               description
                               )
                               values(%s,
                                      %s,
                                      %s,
                                      %s
                            )"""

        with self.con.cursor() as cur:
            cur.execute(
                sql,
                (restaurant.restaurant_name,
                 restaurant.phone_number,
                 restaurant.prefecture_id,
                 restaurant.description))
        self.con.commit()

    def update_shop_data(self, restaurant: Restaurant, uuid: str):
        # DBへ保存
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
        sql = f"""update shops
                            set
                                phone_number = %s,
                                prefecture_id = %s,
                                description = %s,
                                updated_at = %s
                            where id= %s
                            """

        with self.con.cursor() as cur:
            cur.execute(
                sql,
                (restaurant.phone_number,
                 restaurant.prefecture_id,
                 restaurant.description,
                 now,
                 uuid[0][0]
                 ))
        self.con.commit()

    def search_shop_data(self, restaurant: Restaurant):
        # 店舗名が同一のデータがあるかチェック
        sql = f"""select *
                    from shops
                        where name= %s
                            """
        with self.con.cursor() as cur:
            cur.execute(sql, (restaurant.restaurant_name,))
            res = cur.fetchall()

        if res:
            return res
        else:
            return False


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
