import math
from app.car import Car
from app.shop import Shop


class Customer():
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = math.hypot(
            shop.location[0] - self.location[0],
            shop.location[1] - self.location[1]
        )

        fuel_needed = (dist * 2) * (self.car.fuel_consumption / 100)
        fuel_cost = fuel_needed * fuel_price

        products_cost = sum(
            qty * shop.products[prod]
            for prod, qty in self.product_cart.items()
        )

        total = fuel_cost + products_cost
        return round(total, 2)
