from app.classes.product import Products


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: Products
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
