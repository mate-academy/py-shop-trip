from dataclasses import dataclass
from app.convert import shop_list


@dataclass
class Shop:
    name: str
    location: []
    product_list: {}

    def pack_the_bucket(self, wish_list: dict) -> float:
        return (
            sum([wish_list[article] * self.product_list[article]
                for article in wish_list])
        )

    @staticmethod
    def define_shops() -> list:
        shops = []
        for shop in shop_list:
            shops.append(Shop(shop["name"], shop["location"],
                              shop["products"]))
        return shops
