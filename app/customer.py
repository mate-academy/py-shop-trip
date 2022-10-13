from __future__ import annotations
from app.car import Car
from math import dist
from app.shop import Shop


class Customer:
    def __init__(self, customer: dict):
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"]["brand"],
                       customer["car"]["fuel_consumption"])

    def has_enough_money(self, other: float) -> bool:
        return self.money > other

    def trip_to_shop(self, shops: list[Shop], fuel: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        possible_shops = []

        for shop in shops:
            distance = dist(self.location, shop.location)
            cost_of_trip = self.car.trip_cost(distance, fuel) * 2
            purchase = shop.cost_of_products(self.product_cart)
            total = round(purchase + cost_of_trip, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {total}")
            if self.has_enough_money(total):
                possible_shops.append([shop, total])

        if not possible_shops:
            return print(f"{self.name} doesn't have enough "
                         f"money to make purchase in any shop")

        shop, cost = sorted(possible_shops, key=lambda x: x[1])[0]
        print(f"{self.name} rides to {shop.name}\n")
        shop.print_receipt(self.name, self.product_cart)
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - cost} dollars\n")
