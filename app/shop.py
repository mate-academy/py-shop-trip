from typing import List


class Shop:
    def __init__(self, name: str, location: List[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def checkout(self, product_cart: dict) -> float:
        total = 0
        for product, quan in product_cart.items():
            if product in self.products:
                total += self.products[product] * quan
        return total
