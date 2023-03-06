class Shop:
    def __init__(self, shop_info: dict) -> None:
        self.name: str = shop_info["name"]
        self.location: list[int] = shop_info["location"]
        self.assortment: dict = shop_info["products"]
