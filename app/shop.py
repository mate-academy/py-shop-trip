from typing import List, Dict


class Shop:
    def __init__(
            self,
            shop_name: str,
            shop_location: List[float],
            products: Dict[str, float]
    ) -> None:
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.products = products

    def can_sell(self, product_cart: Dict[str, int]) -> bool:
        for product in product_cart:
            if product not in self.products:
                return False
        return True

    def products_cost(self, product_cart: Dict[str, int]) -> float:
        total = 0
        for product, quantity in product_cart.items():
            if product not in self.products:
                raise ValueError(
                    f"Product {product} not available in shop {self.shop_name}"
                )
            total += self.products[product] * quantity
        return round(total, 2)
