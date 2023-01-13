import json
from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    customer_list = list()

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
        self.customer_list.append(self)

    @staticmethod
    def create_from_dict(customers: dict) -> None:
        for customer in customers:
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )

    def cost_of_the_trip(self, shop: Shop) -> float:
        with open("app/config.json", "r") as file:
            json_info = json.load(file)
        fuel_price = json_info["FUEL_PRICE"]

        products_cost = shop.cost_of_all_products(self.product_cart)
        return round((self.car.fuel_consumption / 100)
                     * (dist(self.location, shop.location) * 2)
                     * fuel_price, 2) + products_cost

    def shopping(self, shop: Shop, cheapest_trip: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        print("Date: 04/01/2021 12:33:41\n"
              f"Thanks, {self.name}, for you purchase!\n"
              "You have bought: ")

        for item, amount in self.product_cart.items():
            cost_of_product = amount * shop.products[item]
            print(f"{amount} {item}s for {cost_of_product} dollars")

        print(f"Total cost is "
              f"{shop.cost_of_all_products(self.product_cart)} dollars\n"
              f"See you again!\n\n"
              f"{self.name} rides home\n"
              f"{self.name} now has "
              f"{self.money - cheapest_trip} dollars\n")
