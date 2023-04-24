class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name = shop_info["name"]
        self.location = shop_info["location"]
        self.shop_prod = shop_info["products"]
