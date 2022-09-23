class Shop:
    shops = {}

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict):
        self.name = name
        self.location = location
        self.products = products
        Shop.shops[len(Shop.shops)] = self
