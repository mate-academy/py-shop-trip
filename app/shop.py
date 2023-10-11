from dataclasses import dataclass
from math import sqrt
from decimal import getcontext, Decimal


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_cart_price(self, customer_cart: dict) -> float:
        milk = customer_cart["milk"] * self.products["milk"]
        bread = customer_cart["bread"] * self.products["bread"]
        butter = customer_cart["butter"] * self.products["butter"]
        return milk + bread + butter

    def calculate_trip_price(
            self,
            customer_location: list,
            fuel_price: float,
            fuel_consumption: float,
            customer_cart: dict,
    ) -> float:
        total_cart_price = self.calculate_cart_price(customer_cart)

        distance = sqrt(
            (customer_location[0] - self.location[0]) ** 2
            + (customer_location[1] - self.location[1]) ** 2
        )
        road_price = 2 * (distance * fuel_price * (fuel_consumption / 100))
        getcontext().prec = 2
        return round(float(Decimal(road_price + total_cart_price)), 2)
