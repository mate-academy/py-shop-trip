from app.car import Car
import math


class Customer:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict,
            money: float,
            car: Car,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products
        self.money = money
        self.car = car

    def cost_trip(
            self,
            location: list[int],
            fuel_price: float
    ) -> float:
        distance = math.sqrt(
            (self.location[0] - location[0]) ** 2
            + (self.location[1] - location[1]) ** 2
        )
        cost = round(
            (distance / 100 * self.car.fuel_consumption * fuel_price * 2), 2
        )
        return cost

    def cost_product(
            self,
            products: dict
    ) -> float:
        cost = 0
        for product in products:
            cost += self.products[product] * products[product]
        return round(cost, 2)
