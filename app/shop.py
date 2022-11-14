class Shop:
    shop_list = []

    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        self.shopping_cost = None
