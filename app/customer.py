from __future__ import annotations
import dataclasses
import math
from typing import List


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: "car"

    def get_name(self) -> str:
        return self.name

    def get_product_cart(self) -> dict:
        return self.product_cart

    def get_location(self) -> list:
        return self.location

    def get_money(self) -> float:
        return self.money

    def get_car(self) -> "car":
        return self.car

    def calculate_fuel(
            self,
            home_location: list,
            shop_location: list
    ) -> float:
        shop_distance = math.dist(home_location, shop_location)
        need_fuel = shop_distance * 2 / 100 * self.car.get_fuel_consumption()
        return need_fuel

    def count_purchases(self, shop: "shop") -> float:
        milk_cost = self.get_product_cart()["milk"]\
            * shop["milk"]
        bread_cost = self.get_product_cart()["bread"]\
            * shop["bread"]
        butter_cost = self.get_product_cart()["butter"]\
            * shop["butter"]
        return milk_cost + bread_cost + butter_cost

    def calculate_trip(self, fuel_price: float, shops: List["shop"]) -> tuple:
        best_trip = self.calculate_fuel(
            self.location,
            shops[0].get_location()
        ) * fuel_price + self.count_purchases(shops[0].products)
        best_shop_name = shops[0].name
        for shop in shops:
            transport_cost = self.calculate_fuel(
                self.location,
                shop.get_location(),
            ) * fuel_price
            products_cost = self.count_purchases(shop.products)
            print(f"{self.name}'s trip to the"
                  f" {shop.name} costs "
                  f"{round(transport_cost + products_cost, 2)}")

            if best_trip > transport_cost + products_cost:
                best_trip = transport_cost + products_cost
                best_shop_name = shop.name
        return best_trip, best_shop_name

    def goes_home_from(self, trip_cost: float) -> None:
        rest_customer_money = round(self.get_money() - trip_cost, 2)
        print(
            f"{self.get_name()} rides home\n"
            f"{self.get_name()} now has"
            f" {rest_customer_money} dollars\n"
        )
