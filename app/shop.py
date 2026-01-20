from typing import Dict, Tuple
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: Tuple[int, int],
                 products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def trip_cost(self, customer: Customer, fuel_price: float) -> float:
        distance = customer.distance_to(self.location)
        fuel_to_shop = customer.car.fuel_cost(distance, fuel_price)
        fuel_home = customer.car.fuel_cost(distance, fuel_price)

        product_cost = 0
        for item, qty in customer.product_cart.items():
            if item in self.products:
                product_cost += self.products[item] * qty
            else:
                return float("inf")  # can't fulfill request

        return round(fuel_to_shop + fuel_home + product_cost, 2)

    def can_fulfill_cart(self, cart: Dict[str, int]) -> bool:
        return all(item in self.products for item in cart)
