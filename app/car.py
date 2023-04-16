from app.convert_from_json import FUEL_PRICE

import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = FUEL_PRICE

    def calculate_fuel_consumption_price(
            self,
            customer_location: list[int, int],
            shop_location: list[int, int]
    ) -> float:
        distance = math.dist(customer_location, shop_location)
        fuel_consumption_price = (self.fuel_consumption / 100
                                  ) * self.fuel_price * distance * 2
        return round(fuel_consumption_price, 2)
