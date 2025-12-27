from math import dist

from app.cars import Car


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.car = car
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(*car.values())

    def __repr__(self) -> str:
        return f"Customer: {self.__dict__}"

    def distance(self, shop_location: list) -> float:
        return dist(self.location, shop_location)
