import json


class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]


with open("app/config.json") as file:
    data = json.load(file)

try:
    shops = data["shops"]
    shops_list = [Shop(shop) for shop in shops]
except KeyError:
    raise Exception("Shops data is missing")
