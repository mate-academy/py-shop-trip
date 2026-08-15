from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float | int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def get_distance(self, location: list) -> float:
        return sqrt(
            (self.location[0] - location[0]) ** 2
            + (self.location[1] - location[1]) ** 2
        )

    def calculate_trip_cost(
            self,
            shop: Shop,
            fuel_price: float | int
    ) -> float | int:
        distance_to_shop = self.get_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(
            distance_to_shop * 2,
            fuel_price
        )
        products_cost = shop.get_product_cost(self.product_cart)

        return fuel_cost + products_cost

    def ride_to_shop(self, shop: Shop) -> None:
        self.location = shop.location.copy()
        print(f"{self.name} rides to {shop.name}")

    def ride_home(self) -> None:
        self.location = self.home_location.copy()
        print(f"{self.name} rides home")
