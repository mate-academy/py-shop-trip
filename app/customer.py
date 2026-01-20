import math
from app.car import Car


class Customer:
    def __init__(
        self, name: str,
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

    def calculate_way_price(self,
                            shop_location: list[int],
                            fuel_price: float) -> float:
        distance = math.dist(self.location, shop_location)
        way_price = distance / 100 * self.car.fuel_consumption * 2 * fuel_price
        return round(way_price, 2)
