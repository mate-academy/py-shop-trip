from app.shop.price_list import PriceList


class Shop:
    """A class to create a shop"""
    def __init__(self, items: dict) -> None:
        self.name = items["name"]
        self.location = items["location"]
        self.price_list = PriceList(items["products"])
        self.expenses = None
