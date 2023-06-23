import json


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def shop_create_list() -> list[Shop]:

    shops_list = []

    with open(
            "app/config.json"
    ) as f:
        config = json.load(f)
        for shop_attributes in config["shops"]:
            shop_obj = Shop(**shop_attributes)
            shops_list.append(shop_obj)

        return shops_list
