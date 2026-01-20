class Shop:
    def __init__(self, shop: dict) -> None:
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        self.price_milk = self.products["milk"]
        self.price_bread = self.products["bread"]
        self.price_butter = self.products["butter"]
