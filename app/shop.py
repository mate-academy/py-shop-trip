from decimal import Decimal

class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = [Decimal(str(loc)) for loc in location]
        self.products = {k: Decimal(str(v)) for k, v in products.items()}
