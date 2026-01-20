import math

from app.car import Car


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
        self.__home_location = location

    def initial_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_way_price(self, shop_location: list[int],
                            fuel_price: float) -> float:
        distance = math.dist(self.location, shop_location)
        road_price = self.car.spent_liters_of_fuel(distance) * 2 * fuel_price
        return road_price
