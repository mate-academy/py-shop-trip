from __future__ import annotations

from typing import List
from app.car import Car
from app.store import Shop

import json
import math


class NotEnoughMoneyException(Exception):
    pass


class Customer:
    def __init__(
            self,
            name: str,
            product_cart:
            dict, location:
            list, money: int,
            car: Car) -> None:

        self.name = name
        self.product_cart = product_cart
        self.current_location = location
        self.start_location = location
        self.money = money
        self.car = car
        self.the_cheapest_shop = None
        self.money_needed = None

    @classmethod
    def customers_creating(cls) -> List[Customer]:
        with open("app/config.json", "rb") as config_file:
            config = json.load(config_file)

        customers = [
            cls(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"]
                )
            )
            for customer in config["customers"]]

        return customers

    def print_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculating_distance(self, shop: Shop) -> int | float:
        return math.sqrt(
            ((shop.location[0] - self.current_location[0]) ** 2)
            + ((shop.location[1] - self.current_location[1]) ** 2)

        )

    def calculating_trip_cost(self) -> tuple:
        with open("app/config.json", "rb") as config_file:
            config = json.load(config_file)

        fuel_price = config["FUEL_PRICE"]
        shops = Shop.shops_creating(config)
        overalls = {}

        for shop in shops:
            distance = self.calculating_distance(shop)
            ride_cost = self.car.calculating_ride_cost(distance, fuel_price)
            product_cost = sum(
                self.product_cart[product]
                * shop.products[product] for product in self.product_cart
            )

            money_needed = round(ride_cost + product_cost, 2)
            overalls[money_needed] = shop

            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs "
                f"{round(money_needed, 2)}"
            )

        the_cheapest_shop_info = (sorted(overalls.items())[0])

        return the_cheapest_shop_info

    def go_to_shop(self) -> None:
        shop_info = self.calculating_trip_cost()
        overall_price, shop = shop_info[0], shop_info[1]

        if self.money >= overall_price:
            self.car.drive(self, shop)
            self.the_cheapest_shop = shop
            self.money_needed = overall_price

        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            raise NotEnoughMoneyException

    def making_purchase(self) -> None:
        self.the_cheapest_shop.get_check(self)

    def go_home(self) -> None:
        self.car.drive_home(self)

    def recount_money(self) -> None:
        self.money -= self.money_needed
        print(f"{self.name} now has {self.money} dollars\n")
