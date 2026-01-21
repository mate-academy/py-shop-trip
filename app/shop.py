from app.product import Products


class Shop:
    def __init__(self,
                 name: str,
                 products: Products,
                 location: list) -> None:
        self.name = name
        self.products = products
        self.location = location
