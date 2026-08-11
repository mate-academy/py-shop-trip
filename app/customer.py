import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            money: float,
            location: list,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.money = money
        self.location = location
        self.car = car

    def get_distance_to(self, shop_location: list) -> float:
        return math.dist(self.location, shop_location)

    def get_ride_cost(self, distance: float, fuel_price: float) -> float:
        return distance * 2 * fuel_price * self.car["fuel_consumption"] / 100
