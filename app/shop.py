from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_purchase(self, product_cart: dict) -> float:
        result = 0
        for product, amount in product_cart.items():
            result += amount * self.products[product]
        return result
