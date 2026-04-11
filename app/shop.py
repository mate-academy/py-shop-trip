from app.location import Location
from app.product import Product


class Shop:
    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = Location(*location)
        self.products = Product(**products)
