from __future__ import annotations


class Shop:
    def __init__(self, shops_dict: dict) -> None:
        self.shops_dict = shops_dict

    @property
    def name(self) -> str:
        return self.shops_dict["name"]

    @property
    def product_price(self) -> dict:
        return self.shops_dict["products"]

    @property
    def location(self) -> list[int]:
        return self.shops_dict["location"]
