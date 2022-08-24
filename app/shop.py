from app.location import Location


class Shop:
    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = Location(shop["location"])
        self.products = shop["products"]

    def get_price(self, product_name: dict) -> float:
        return self.products[product_name]
