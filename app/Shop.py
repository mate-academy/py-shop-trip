from typing import Dict


class Shop:
    def __init__(self, name: str,
                 products: Dict[str, float],
                 location: str) -> None:
        self.name = name
        self.products = products
        self.location = location

    def calculate_purchase_cost(self, product_cart: Dict[str, int]) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += self.products.get(product, 0) * quantity
        return round(total_cost, 2)

    def is_product_available(self, product_cart: Dict[str, int]) -> bool:
        for product in product_cart:
            if product not in self.products:
                return False
        return True
