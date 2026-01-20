from __future__ import annotations
from dataclasses import dataclass
from typing import Union


@dataclass
class ShopProduct:
    name: str
    price: Union[int, float]
    product_collaction: dict[ShopProduct] = None

    @classmethod
    def create_shop_product_collaction(
        cls, dict_of_shop_products: dict
    ) -> dict[ShopProduct]:
        return {
            name: cls(name=name, price=price)
            for name, price in dict_of_shop_products.items()
        }


@dataclass
class ClientCart:
    name: str
    count: int

    @staticmethod
    def create_cliet_wish_list(
        dict_of_client_products: dict,
    ) -> dict[ClientCart]:
        return {
            name: ClientCart(name=name, count=count)
            for name, count in dict_of_client_products.items()
        }
