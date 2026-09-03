from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location.copy()
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def calculate_distance(
        self,
        destination: list[int]
    ) -> float:
        return dist(self.location, destination)

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: float
    ) -> float:
        distance_to_shop = self.calculate_distance(
            shop.location
        )

        fuel_cost_to_shop = self.car.calculate_fuel_cost(
            distance=distance_to_shop,
            fuel_price=fuel_price
        )

        fuel_cost_to_home = self.car.calculate_fuel_cost(
            distance=distance_to_shop,
            fuel_price=fuel_price
        )

        products_cost = shop.product_cost(
            self.product_cart
        )

        total_trip_cost = (
            fuel_cost_to_shop
            + products_cost
            + fuel_cost_to_home
        )

        return total_trip_cost

    def ride_to(
        self,
        destination: list[int]
    ) -> None:
        self.location = destination.copy()

    def has_enough_money(
        self,
        amount: float
    ) -> bool:
        return self.money >= amount

    def pay(
        self,
        amount: float
    ) -> None:
        self.money -= amount
