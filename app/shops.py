class Shops:
    def __init__(self,
                 shop_name: str,
                 shop_location: list[int],
                 products: dict) -> None:
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.products = products
