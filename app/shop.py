from app.product import Product


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int | float],
            products: dict) -> None:
        self.name = name
        self.location = location
        self.products = [
            Product(key, value) for key, value in products.items()
        ]
