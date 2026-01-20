from app.config import data_config


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


shops = []
for shop in data_config["shops"]:
    shop = Shop(shop["name"], shop["location"], shop["products"])
    shops.append(shop)
