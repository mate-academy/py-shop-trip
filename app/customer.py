import math

from app.car import Car


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int,
                 car: Car) -> None:
        self.car = car
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.__home_location = location

    def initial_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def price_way_to_shop_or_home(self,
                                  shop_location: list[int],
                                  fuel_price: float) -> float:
        distance = math.dist(self.location, shop_location)
        road_price = self.car.gas_for_distance(distance) * 2 * fuel_price
        return road_price
