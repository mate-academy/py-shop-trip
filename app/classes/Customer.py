import json
from dataclasses import dataclass
from math import sqrt
from datetime import datetime

with open("../app/config.json", "r") as f:
    file = json.load(f)

FUEL_PRICE = file["FUEL_PRICE"]


@dataclass()
class Customer:
    def __init__(self, name, product_cart, home_location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.home_location = home_location
        self.money = money
        self.car = car
        self.location = home_location

    def trip_cost(self, shop):
        x_1 = self.location[0]
        x_2 = shop.location[0]
        y_1 = self.location[1]
        y_2 = shop.location[1]
        distance_to_shop = sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
        fuel_price_per_100 = self.car.fuel_consumption * FUEL_PRICE
        trip_coast = 2 * distance_to_shop * fuel_price_per_100 / 100
        shoping_cost = 0
        for product in self.product_cart:
            shoping_cost += self.product_cart[product] * shop.products[product]
        cost = round(trip_coast + shoping_cost, 2)
        return cost

    def print_all_store_costs(self, shops):
        for shop in shops:
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {self.trip_cost(shop)}")

    def cheapest_way(self, shops):
        cheapest = min(shops, key=lambda shop: self.trip_cost(shop))
        return cheapest

    def go_to_shop(self, shop):
        print(f"{self.name} rides to {shop.name}\n")
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        self.location = shop.location

        print(f"Date: {date_time}\n"
              f"Thanks, {self.name}, for you purchase!""")

    def make_shopping(self, shop):
        print("You have bought: ")
        total = 0
        for product in self.product_cart:
            total += self.product_cart[product] * shop.products[product]
            print(f"{self.product_cart[product]} {product}s "
                  f"for {shop.products[product] * self.product_cart[product]} "
                  f"dollars")
        print(f"Total cost is {round(total, 2)} dollars\n"
              f"See you again!\n")

    def go_to_home(self, shop):
        self.location = self.home_location
        print(f"{self.name} rides home\n"
              f"{self.name} now has "
              f"{self.money - self.trip_cost(shop)} dollars\n")
