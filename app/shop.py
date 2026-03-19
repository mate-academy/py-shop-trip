class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]
