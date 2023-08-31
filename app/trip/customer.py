from __future__ import annotations
import dataclasses
import math

from app.trip.car import Car
import app.shop as shop_m


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car
    possible_trips = {}

    def count_money(self, has_shopped: bool = False) -> int | float:
        if has_shopped:
            self.money = round(self.money, 2)
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} has {self.money} dollars")
        return self.money

    def calculate_distance_to_shop(self, shop: shop_m.Shop) -> float:
        x1 = self.location[0]
        y1 = self.location[1]
        x2 = shop.location[0]
        y2 = shop.location[1]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def calculate_products_cost(self, shop: shop_m.Shop) -> float | int:
        products_cost = 0
        for product, amount in self.product_cart.items():
            products_cost += shop.products[product] * amount
        if isinstance(products_cost, float):
            return round(products_cost, 1)
        return products_cost

    def calculate_trip_cost(self, shop: shop_m.Shop) -> float:
        distance = self.calculate_distance_to_shop(shop)
        fuel_cost = self.car.calculate_fuel_cost(distance)
        products_cost = self.calculate_products_cost(shop)
        total = round(products_cost + fuel_cost, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {total}")
        self.possible_trips[total] = shop
        return total

    def decision(self) -> None | shop_m.Shop:
        if self.money < min(self.possible_trips):
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return None
        optimal_decision = self.possible_trips[min(self.possible_trips)]
        print(f"{self.name} rides to {optimal_decision.name}")
        self.location = optimal_decision.location
        self.money -= min(self.possible_trips)
        return optimal_decision

    def go_home(self) -> None:
        print(f"{self.name} rides home")

    @classmethod
    def from_dict(cls, dict_: dict, fuel_price: float) -> Customer:
        return Customer(
            dict_.get("name"),
            dict_.get("product_cart"),
            dict_.get("location"),
            dict_.get("money"),
            Car(
                dict_["car"]["brand"],
                dict_["car"]["fuel_consumption"],
                fuel_price
            )
        )
