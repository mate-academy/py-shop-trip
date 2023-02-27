import math
from car import Car


class Customer:

    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int | float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"],
                       car["fuel_consumption"])

    def distance(self,
                 customer_location: list,
                 shop_location: list) -> int | float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def trip_cost(self, distance: int | float,
                  fuel_price: int | float,
                  products: dict) -> int | float:
        product_cost = []
        for key, value in self.product_cart.items():
            product_cost.append(self.product_cart[key] * products[key])
        fuel_consumption = ((self.car.fuel_consumption * distance) / 100)
        final_price = (fuel_consumption * fuel_price) + sum(product_cost)

        return final_price
