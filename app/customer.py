from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def trip_costs(self, shop: Shop) -> float:
        distance = sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        total_consumption = (distance * self.car.fuel_consumption) / 100
        return round(total_consumption * self.car.FUEL_PRICE * 2, 2)

    def trip_costs_announcer(self, shop: Shop) -> str:
        fuel_cost = self.trip_costs(shop)
        products_cost = shop.calculate_cart_cost(self.product_cart)
        sum_ = fuel_cost + products_cost
        return f"{self.name}'s trip to the {shop.name} costs {sum_}"

    def go_to_shop(self, shop_name: str) -> str:
        return f"{self.name} rides to {shop_name}"

    def go_home(self) -> str:
        return f"{self.name} rides home"
