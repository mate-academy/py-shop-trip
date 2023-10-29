import datetime
import math
from typing import List
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float | int
    car: Car

    def calculate_product_cost(self,
                               shop: Shop) -> dict:
        total = 0
        purchases = {}
        for item in self.product_cart.keys():
            if item in shop.products.keys():
                total += shop.products[item] * self.product_cart[item]
                purchases[item] = round(
                    shop.products[item] * self.product_cart[item], 2
                )
        return purchases

    def print_receipt(self,
                      shop: Shop,
                      purchases: dict) -> None:
        purchase_date = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S")
        print(f"Date: {purchase_date}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              f"You have bought: ")

        for key in self.product_cart.keys():
            amount = self.product_cart[key] * shop.products[key]
            if isinstance(amount, float) and amount.is_integer():
                amount = math.floor(amount)
            print(f"{self.product_cart[key]} {key}s for {amount} dollars")

        print(f"Total cost is {round(sum(purchases.values()), 2)} dollars\n"
              f"See you again!\n")

    def print_trip(self, fuel_cost: float, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        total_costs = []
        for shop in shops:
            cost = (sum(self.calculate_product_cost(shop).values())
                    + self.car.calculate_fuel_price(fuel_cost,
                                                    self.location,
                                                    shop.location)
                    )
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")
            total_costs.append(cost)

        total_purchase = min(total_costs)
        if self.money >= total_purchase:
            selected_shop = shops[total_costs.index(total_purchase)]
            print(f"{self.name} rides to {selected_shop.name}\n")
            self.print_receipt(
                selected_shop,
                self.calculate_product_cost(selected_shop)
            )
            print(f"{self.name} rides home\n"
                  f"{self.name} now has "
                  f"{self.money - min(total_costs)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
