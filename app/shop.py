from app.products import Products


class Shop:
    shops = []

    def __init__(self,
                 name: str,
                 location: list,
                 products: Products
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops.append(self)
