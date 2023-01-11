import json
from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def cost_of_the_trip(self, shop: Shop) -> float:
        with open("app/config.json", "r") as file:
            json_info = json.load(file)
        fuel_price = json_info["FUEL_PRICE"]

        return round((self.car.fuel_consumption / 100)
                     * (dist(self.location, shop.location) * 2)
                     * fuel_price, 2)
