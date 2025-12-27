from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_products(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * value
            for product, value
            in product_cart.items()
        )
