from typing import Dict, Tuple


class Shop:
    def __init__(
            self,
            name: str,
            location: Tuple[int, int],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_total_cost(self, product_cart: Dict[str, int]) -> float:
        total = 0
        for product, quantity in product_cart.items():
            product_price = self.products.get(product, 0)
            total += product_price * quantity
        return total
