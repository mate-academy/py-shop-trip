from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float | int
    car: Car
    home_location: list[int] = field(init=False)

    def __post_init__(self) -> None:
        """Викликається автоматично одразу після __init__"""
        self.home_location = self.location.copy()

    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        """Factory method for Customer class"""
        car = Car(**data["car"])
        return cls(
            name=data["name"],
            product_cart=data["product_cart"],
            location=data["location"],
            money=data["money"],
            car=car
        )

    def distance_to_shop(self, destination_location: list[int]) -> float:
        """Counting distance to shop and home"""
        cust_x, cust_y = self.location
        shop_x, shop_y = destination_location
        distance = math.sqrt(
            (cust_x - shop_x) ** 2 + (cust_y - shop_y) ** 2
        ) * 2
        return round(distance, 2)

    def cart_price(self, product_prices: dict) -> float | int:
        """Counting cart price for expect shop"""
        total_product_price = 0
        for product, number in self.product_cart.items():
            total_product_price += product_prices[product] * number

        if total_product_price == int(total_product_price):
            return int(total_product_price)

        return round(total_product_price, 2)

    def trips_cost(self, shops: list[Shop], fuel_price: int | float) -> dict:
        """Creating dict with total prices for each shop"""
        shops_cost = {}
        for shop in shops:
            distance_to_shop = self.distance_to_shop(shop.location)
            cost_for_1_km = self.car.cost_for_1_km(fuel_price)

            road_cost = distance_to_shop * cost_for_1_km
            total_trip_cost = road_cost + self.cart_price(shop.products)
            shops_cost[shop.name] = round(total_trip_cost, 2)
        return shops_cost

    def find_min_trip_cost(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> Shop | None:
        """Finding shop with min trip cost"""
        costs_dict = self.trips_cost(shops, fuel_price)

        cheapest_shop_name = min(costs_dict, key=costs_dict.get)
        for shop in shops:
            if shop.name == cheapest_shop_name:
                return shop
        return None

    def possibility_of_the_trip(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> bool:
        """Checking if shop trip possibility exists"""
        costs = self.trips_cost(shops, fuel_price)
        min_cost = min(costs.values())
        return self.money >= min_cost

    def trip_info(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> None:
        """Printing trips info messages"""
        currency = "dollars" if self.money != 1 else "dollar"
        print(f"{self.name} has {self.money} {currency}")

        costs = self.trips_cost(shops, fuel_price)
        for shop, price in costs.items():
            trip_message = (
                f"{self.name}'s trip to the {shop} costs {price}"
            )
            print(trip_message)

        if not self.possibility_of_the_trip(shops, fuel_price):
            print(
                f"{self.name} doesn't have enough money to "
                f"make a purchase in any shop"
            )
            return

        best_shop = self.find_min_trip_cost(shops, fuel_price)
        trip_cost = costs[best_shop.name]
        print(f"{self.name} rides to {best_shop.name}\n")
        self.location = best_shop.location

        best_shop.print_receipt(self)

        print(f"\n{self.name} rides home")
        self.location = self.home_location

        self.money = round(self.money - trip_cost, 2)
        currency_left = "dollars" if self.money != 1 else "dollar"
        print(f"{self.name} now has {self.money} {currency_left}\n")
