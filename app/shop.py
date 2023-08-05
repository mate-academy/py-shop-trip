

class Shop:

    def __init__(self,
                 name: str,
                 shop_location: list[int, int],
                 products: dict
                 ) -> None:
        self.name = name
        self.location = shop_location
        self.products = products
