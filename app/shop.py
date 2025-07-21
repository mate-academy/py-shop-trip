import json


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products


with open("app/config.json") as config:
    data = json.load(config)
    shop_list = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"])
        for shop in data["shops"]]
