class Shop:
    list_shops = []

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.list_shops.append(self)
