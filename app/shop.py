class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.products = products
        self.location = location
        self.name = name


def create_shop(shop: dict) -> Shop:
    return Shop(name=shop["name"],
                location=shop["location"],
                products=shop["products"])
