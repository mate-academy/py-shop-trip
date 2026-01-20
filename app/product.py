from __future__ import annotations

from decimal import Decimal


class Product:
    def __init__(
            self,
            name: str,
            price: Decimal = None,
            quantity: int = None,
    ) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_cost(self, price: Decimal) -> Decimal:
        return self.quantity * price

    @staticmethod
    def calculate_total_cost(
            custom_prod: list[Product],
            shop_prod: list[Product]
    ) -> Decimal:
        products_price = {product.name: product.price for product in shop_prod}
        return Decimal(sum(
            product.calculate_cost(products_price.get(product.name))
            for product in custom_prod
        ))

    @classmethod
    def get_products(
            cls,
            shop_products: dict[str, float] = None,
            product_cart: dict[str, int] = None,
    ) -> list[Product]:
        if shop_products:
            return [
                cls(
                    name=name,
                    price=Decimal(str(price)).quantize(Decimal("0.1"))
                )
                for name, price in shop_products.items()
            ]

        if product_cart:
            return [
                cls(name=name, quantity=quantity)
                for name, quantity in product_cart.items()
            ]
