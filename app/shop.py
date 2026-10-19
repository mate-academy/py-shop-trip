import math
from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
            self, name: str, location: List[float], products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, location: List[float]) -> float:
        return math.dist(self.location, location)

    def products_cost(self, cart: Dict[str, int]) -> float:
        return sum(
            qty * self.products[prod]
            for prod, qty in cart.items()
            if prod in self.products
        )

    def calculate_trip_cost(
            self, customer: "Customer", fuel_price: float
    ) -> float:
        distance = self.calculate_distance(customer.location)
        fuel_cost = customer.car.calculate_fuel_cost(
            distance * 2, fuel_price
        )
        return round(fuel_cost + self.products_cost(customer.product_cart), 2)
