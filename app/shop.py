from decimal import Decimal
from app.product import Product


class Shop:

    def __init__(
            self,
            name: str,
            location: list,
            products: list[Product]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_price(self, product_name: str) -> Decimal:
        return (
            next(product.price for product in self.products
                 if product_name == product.name)
        )
