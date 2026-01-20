from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def product_cost(self, product_name: str, quantity: int) -> Decimal:
        product_cost = (Decimal(str(self.products[product_name]))
                        * Decimal(quantity))
        if product_cost % 1 == 0:
            return product_cost.quantize(Decimal("0"))
        return product_cost

    def calc_total_cost(self, product_cart: dict) -> Decimal:
        return Decimal(str(sum(Decimal(str(self.products[product]))
                               * Decimal(str(product_cart[product]))
                               for product in product_cart)))
