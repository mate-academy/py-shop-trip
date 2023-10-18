from __future__ import annotations

import datetime
import math
from dataclasses import dataclass
from typing import List

from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: float | int
    car: dict

    def _fuel_costs(self, fuel_price: float, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location

        distance = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)
        cost_both_ways = round(
            (fuel_price * distance * self.car["fuel_consumption"] / 100 * 2), 2
        )
        return cost_both_ways

    def _products_coasts(self, shop: Shop) -> float:
        cost = 0
        for key in self.product_cart.keys():
            cost += self.product_cart[key] * shop.products[key]
        return cost

    def print_the_trip(
            self,
            fuel_price: float,
            shops_list: List[Shop]
    ) -> None:
        print(f"{self.name} has {self.money} dollars")

        trips_costs = {}
        for shop in shops_list:
            trip_costs = sum((
                self._fuel_costs(fuel_price, shop),
                self._products_coasts(shop)
            ))
            print(f"{self.name}'s trip to the {shop.name} costs {trip_costs}")
            trips_costs[shop.name] = trip_costs

        shop_name_to_go = min(trips_costs, key=trips_costs.get)
        shop_to_go = next((
            shop for shop in shops_list if shop.name == shop_name_to_go
        ))

        if trips_costs[shop_name_to_go] <= self.money:
            print(f"{self.name} rides to {shop_name_to_go}\n")

            self._print_receipt(shop_to_go)

            remainder = self.money - trips_costs[shop_name_to_go]
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {remainder} dollars\n"
            )
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

    def _print_receipt(self, shop: Shop) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S")
        print(
            f"Date: {now}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought: "
        )

        for key in self.product_cart.keys():
            amount = self.product_cart[key] * shop.products[key]
            if isinstance(amount, float) and amount.is_integer():
                amount = int(amount)
            print(f"{self.product_cart[key]} {key}s for {amount} dollars")

        print(
            f"Total cost is {self._products_coasts(shop)} dollars\n"
            f"See you again!\n"
        )
