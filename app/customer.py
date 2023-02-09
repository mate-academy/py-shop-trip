from __future__ import annotations
from typing import List

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

    @classmethod
    def make_instance(cls, customer: dict) -> Customer:
        return cls(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car.make_instance(customer["car"])
        )

    def calculate_trip_costs(self,
                             shops: List[Shop],
                             fuel_price: float) -> str | Shop:
        trip_costs = {}
        for shop in shops:
            trip_cost = 2 * (((shop.location[0] - self.location[0]) ** 2
                              + (shop.location[1] - self.location[1]) ** 2)
                             ** (1 / 2)) * (self.car.fuel_consumption
                                            * fuel_price / 100)
            for product_item in self.product_cart:
                trip_cost += self.product_cart[product_item] * shop.products[product_item]
            trip_cost = round(trip_cost, 2)
            trip_costs[trip_cost] = shop
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
        min_trip_cost = min(trip_costs.keys())
        if min_trip_cost <= self.money:
            self.money -= min_trip_cost
            return trip_costs[min_trip_cost]
        else:
            return "not_enough_money"
