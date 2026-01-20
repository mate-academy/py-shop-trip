class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
