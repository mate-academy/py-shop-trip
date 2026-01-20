import json
import math
from app.car import Car
import app.shops as sh


class Customers:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def create_customers_list() -> list:
        with open("app/config.json") as config:
            info = json.load(config)
        customer_ls = []
        for customer in info["customers"]:
            new_customer = Customers(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    consumption=customer["car"]["fuel_consumption"],
                    fuel_price=info["FUEL_PRICE"]
                ))
            customer_ls.append(new_customer)
        return customer_ls

    def count_road_price(self, shop: sh.Shops) -> float:
        road_km = math.floor(
            math.dist(self.location, shop.location) * 2 * 100
        ) / 100
        trip_cost = round(
            (self.car.fuel_price * road_km * self.car.consumption / 100), 2)
        return trip_cost

    def count_grocery_price(self, shop: sh.Shops) -> float:
        products_cost = 0
        for goods, amount in self.product_cart.items():
            products_cost += amount * shop.products[goods]
        return products_cost
