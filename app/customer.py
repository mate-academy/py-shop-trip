from __future__ import annotations
from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self, name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)
        self.cheapest_shop = None
        self.enough_money = False
        self.total_cost = 0

    def choose_the_best_shop(
            self,
            shops_list: List[Shop],
            fuel_price: float
    ) -> None:
        shops = {}
        for shop in shops_list:
            costs_of_product = shop.calculate_amount_for_products(
                self.product_cart
            )
            fuel_cost = self.car.calculate_fuel_cost(
                self.location, shop.location, fuel_price
            )
            shops[shop] = round(costs_of_product + fuel_cost, 2)

        self.cheapest_shop = min(shops, key=shops.get)
        if self.money >= shops[self.cheapest_shop]:
            self.enough_money = True
            self.total_cost = round(shops[self.cheapest_shop], 2)

        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            print(f"{self.name}'s trip to the {shop.name} costs {shops[shop]}")

    def ride_to_the_shop(self) -> None:

        if self.enough_money:
            print(f"{self.name} rides to {self.cheapest_shop.name}\n")
            self.location = self.cheapest_shop.location
        else:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )

    def buy_products(self) -> None:
        if self.enough_money:
            self.cheapest_shop.print_bill(
                self.product_cart, self.name
            )

            self.money -= self.total_cost

    def ride_to_home(self) -> None:
        if self.enough_money:
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {self.money} dollars\n"
            )

    @classmethod
    def create_customers(cls, customers: List) -> List[Customer]:
        return [cls(**customer) for customer in customers]
