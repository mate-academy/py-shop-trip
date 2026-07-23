import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car_data: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = location.copy()
        self.location = location.copy()
        self.money = money
        self.car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )

    def distance_between(self, loc1: list[int], loc2: list[int]) -> float:
        """Обчислює евклідову відстань між двома точками."""
        return math.sqrt((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        """Обчислює повну вартість від ДОМУ до магазину і назад."""
        distance = self.distance_between(self.home_location, shop.location)
        round_trip_fuel_cost = \
            (self.car.calculate_fuel_cost(distance, fuel_price) * 2)
        products_cost = shop.calculate_products_cost(self.product_cart)
        return round_trip_fuel_cost + products_cost
