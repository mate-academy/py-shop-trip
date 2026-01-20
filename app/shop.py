from typing import Dict, List


class Shop:
    def __init__(
        self,
        name: str,
        location: List[float],
        products: Dict[str, float]
    ) -> None:
        self.name: str = name
        self.location: List[float] = location
        self.products: Dict[str, float] = products

    def purchase(self, product_cart: Dict[str, int]) -> float:
        price: float = 0.0
        for key, quantity in product_cart.items():
            if key in self.products:
                price += quantity * self.products[key]
        return round(price, 2)
