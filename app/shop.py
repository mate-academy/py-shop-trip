from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    @staticmethod
    def read_shop_json(data: list) -> list:
        return [Shop(**shop) for shop in data]
