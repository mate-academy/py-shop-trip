from app.car import Car
import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def calculate_trip_cost(self, shop: dict, fuel_price: float) -> float:
        total = 0
        for product, amount in self.product_cart.items():
            if product not in shop.products:
                return None
            price = amount * shop.products[product]
            total += price
        distance = self.calculate_distance(self.location, shop.location)
        total += self.car.calculate_cost_fuel(distance, fuel_price) * 2
        return total

    def calculate_distance(self, loc1: list, loc2: list) -> float:
        x1, y1 = loc1
        x2, y2 = loc2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
