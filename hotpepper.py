from __future__ import annotations
from typing import OrderedDict
from lxml import etree
import requests as rq

import scrape_base
import const
import lib


class HotPepper(scrape_base.Scrape_Base):
    def scrape_restaurant(self, file_text: str) -> None:
        root: etree.Element = etree.fromstring(file_text.encode('utf-8'))

        for restaurant in root.xpath(
                './/ns:shop',
                namespaces={
                'ns': "http://webservice.recruit.co.jp/HotPepper/"}):

            # 店名
            shop_name: etree.Element = restaurant.xpath(
                './/ns:name',
                namespaces={
                    'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            # スペースがある場合削除
            shop_name = lib.remove_spaces(shop_name)

            # 住所
            address = restaurant.xpath(
                './/ns:address',
                namespaces={
                    'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            # 地域
            prefecture = restaurant.xpath(
                './/ns:service_area/ns:name',
                namespaces={
                    'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            if prefecture == "東京":
                prefecture = "東京都"
            elif prefecture == "大阪":
                prefecture == "大阪府"
            elif prefecture == "京都":
                prefecture = "京都府"
            elif "県" not in prefecture:
                prefecture = prefecture + "県"

            prefecture_id = const.prefecture_dic[prefecture]

            # city = restaurant.xpath(
            #     './/ns:middle_area/ns:name',
            #     namespaces={
            #         'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            # 電話番号 なし

            # リンク先
            link_url = restaurant.xpath(
                './/ns:urls/ns:pc',
                namespaces={
                    'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            # 説明
            description = restaurant.xpath(
                './/ns:catch',
                namespaces={
                    'ns': "http://webservice.recruit.co.jp/HotPepper/"})[0].text

            restaurant_info = scrape_base.Restaurant(
                shop_name, None, address, prefecture_id, description, link_url)

            # 既存データがあるかどうか
            res_uuid = self.search_shop_data(restaurant_info)
            if res_uuid:
                self.update_shop_data(restaurant_info, res_uuid)
            else:
                # 保存処理
                self.save_shop_data(restaurant_info)
