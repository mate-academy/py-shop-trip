from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    @classmethod
    def get_shop_instance(cls, shop: dict):
        return cls(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
