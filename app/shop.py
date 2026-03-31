from typing import Any


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, float]
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products


def create_shop(data: Any) -> list[Shop]:
    shops = []
    for shop in data["shops"]:
        shops.append(Shop(shop["name"],
                          shop["location"],
                          shop["products"]
                          ))
    return shops
