from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str: int | float]

    @classmethod
    def create_shops(cls, shops: dict) -> list:
        return [
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            for shop in shops
        ]
