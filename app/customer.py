from math import sqrt

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def road_cost(self, end_point: list, fuel_price: float) -> float:
        road_km = sqrt((self.location[0] - end_point[0]) ** 2
                       + (self.location[1] - end_point[1]) ** 2)
        return fuel_price * road_km * self.car.fuel_consumption / 100
