class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def create_stores(list_shops: dict) -> dict:
    shops = {}
    for shop in list_shops:
        shops[shop["name"]] = Shop(shop["name"],
                                   shop["location"],
                                   shop["products"])
    return shops
