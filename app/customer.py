from __future__ import annotations

import math

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
    def from_dict(cls, customer_info: dict) -> Customer:
        return cls(customer_info["name"],
                   customer_info["product_cart"],
                   customer_info["location"],
                   customer_info["money"],
                   Car.from_dict(customer_info["car"]))

    def distance_to_shop(self, shop: Shop) -> float:
        distance = math.sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        return distance

    def trip_to_shop_cost(self,
                          shop: Shop,
                          fuel_price: float) -> float:
        road_cost = round(
            self.car.consumption / 100
            * self.distance_to_shop(shop)
            * fuel_price * 2, 2
        )
        food_cost = 0
        for item in self.product_cart:
            food_cost += round(
                shop.products[item]
                * self.product_cart[item], 2
            )
        return road_cost + food_cost

    def choose_shop(self, shops: list, fuel_price: float) -> Shop | None:
        shops_can_go = {}
        for shop in shops:
            trip_cost = self.trip_to_shop_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{trip_cost}")
            if trip_cost <= self.money:
                shops_can_go[shop] = trip_cost
        if shops_can_go:
            return min(shops_can_go.items(), key=lambda x: x[1])[0]
        return
