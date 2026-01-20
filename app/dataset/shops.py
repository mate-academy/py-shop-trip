import json

from app.classes.product import Products
from app.classes.shop import Shop


def get_all_shops() -> list:
    shops = []
    with open("app/config.json", "r") as file:
        date_from_file = json.load(file)
        for shop in date_from_file["shops"]:
            shops.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    Products(
                        shop["products"]["milk"],
                        shop["products"]["bread"],
                        shop["products"]["butter"]
                    )
                )
            )
        return shops
