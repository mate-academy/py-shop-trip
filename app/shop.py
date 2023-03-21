class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name = shop_info.get("name")
        self.location = shop_info.get("location")
        self.products = shop_info.get("products")
