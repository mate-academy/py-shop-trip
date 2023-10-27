from __future__ import annotations
from typing import List
import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float | int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def shopping(self, shops: List[Shop], fuel_price: float | int) -> None:
        self.__check_money()
        self.get_shop(shops, fuel_price)

    def __calculate_cost_trip(
            self,
            fuel_price: float | int,
            distance: int | float
    ) -> float:
        return round(
            self.car.fuel_consumption / 100 * distance * fuel_price * 2,
            2
        )

    def get_shop(self, shops: List[Shop], fuel_price: int | float) -> None:
        self_x, self_y = self.location
        best_shop = {"total_cost": None, "shop": None}

        for shop in shops:
            total_cost = 0
            total_shop = best_shop["total_cost"]
            shop_x, shop_y = shop.location
            distance = math.sqrt(
                (self_x - shop_x) ** 2 + (self_y - shop_y) ** 2
            )
            total_cost += self.__calculate_cost_trip(fuel_price, distance)
            total_cost += self.__calculate_money_for_products(shop.products)

            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost <= self.money and (
                    not total_shop or total_shop > total_cost
            ):
                best_shop = {"total_cost": total_cost, "shop": shop}
        if best_shop["shop"]:
            total_cost, shop = best_shop.values()
            print(f"{self.name} rides to {shop.name}\n")
            self.location = best_shop["shop"].location
            shop.bill(self.name, self.product_cart)
            print(f"{self.name} rides home")
            self.location = [self_x, self_y]
            print(f"{self.name} now has {self.money - total_cost} dollars\n")
        else:
            print(
                f"{self.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )

    def __check_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def __calculate_money_for_products(self, products: dict) -> float:
        return sum(
            round(products[product] * quantity, 2)
            for product, quantity in self.product_cart.items()
        )
