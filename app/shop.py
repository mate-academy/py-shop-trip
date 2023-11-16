import json


with open("app/config.json", "r") as j_file:
    shop = json.load(j_file)["shops"]


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
