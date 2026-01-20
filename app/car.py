import math
from app.shop import Shop


class Car:
    def __init__(self, car: dict) -> None:
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]

    @staticmethod
    def round_distance(number: float) -> float | int:
        if round(number * 1000) % 5 == 0 and round(number * 1000) % 10 == 5:
            return number - 0.001
        else:
            return number

    def trip_cost(self,
                  customer_location: list,
                  shop: Shop,
                  fuel_price: float) -> float:

        customer_x, customer_y = customer_location
        shop_x, shop_y = shop.location

        distance = round(math.sqrt((shop_x - customer_x) ** 2 + (shop_y - customer_y) ** 2), 2)  # noqa: E501
        cost = round(((self.fuel_consumption / 100) * distance * fuel_price) * 2, 3)  # noqa: E501
        return round(self.round_distance(cost), 2)
