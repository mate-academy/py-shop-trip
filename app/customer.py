from __future__ import annotations
import math
from dataclasses import dataclass
from app.car import Car
from datetime import datetime
from app.shop import Shop


class NotEnoughMoney(Exception):

    def __init__(self) -> None:
        super().__init__()


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def get_info_customer(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_cheapest_trip(self, shops: list, fuel_price: float) -> tuple:
        travel_costs = {}
        for shop in shops:
            cost_road = self.calculate_cost_road(shop, fuel_price)
            cost_products = self.calculate_cost_products(shop.products)
            costs = cost_road + cost_products
            print(f"{self.name}'s trip to the {shop.name} costs {costs}")
            travel_costs[shop] = costs
        cheapest_shop, cheapest_price = (
            min(travel_costs.items(), key=lambda x: x[1])
        )
        if self.money < cheapest_price:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            raise NotEnoughMoney
        print(f"{self.name} rides to {cheapest_shop.name}")
        print("")
        return cheapest_shop, cheapest_price

    def calculate_cost_products(self, price: float) -> float:
        cost_products = 0
        for product in self.product_cart:
            cost_products += price[product] * self.product_cart[product]
        return cost_products

    def calculate_cost_road(self, shop: dict, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        need_fuel = (distance / 100) * self.car.fuel_consumption
        cost_road = (need_fuel * fuel_price) * 2
        return round(cost_road, 2)

    def calculate_distance(self, shop_location: list) -> float:
        return math.sqrt(
            (
                (self.location[0] - shop_location[0]) ** 2
                + (self.location[1] - shop_location[1]) ** 2
            )
        )

    def shop_trip(self, shop: Shop) -> None:
        print(f"Date: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        check_amount = 0
        for product in self.product_cart:
            product_price = self.product_cart[product] * shop.products[product]
            check_amount += product_price
            if product_price == int(product_price):
                product_price = int(product_price)
            print(f"{self.product_cart[product]} {product}s "
                  f"for {product_price} dollars")
        print(f"Total cost is {check_amount} dollars")
        print("See you again!")
        print("")

    def result(self, money_spent: float) -> None:
        rest_money = self.money - money_spent
        print(f"{self.name} rides home")
        print(f"{self.name} now has {rest_money} dollars")
        print("")
