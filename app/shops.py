class Shop:
    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.product = shop["products"]
