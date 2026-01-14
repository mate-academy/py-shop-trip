import math
from typing import Dict, List
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: List[float],
        money: float,
        car: Dict[str, float]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
        self.home_location = location[:]  # копія початкової локації

    def distance_to(self, shop_location: List[float]) -> float:
        return math.dist(self.location, shop_location)

    def products_total(self, shop_products: Dict[str, float]) -> float:
        return sum(
            shop_products[prod] * qty
            for prod, qty in self.product_cart.items()
        )

    def go_to(self, location: List[float]) -> None:
        self.location = location[:]

    def go_home(self) -> None:
        self.go_to(self.home_location)
