from dataclasses import dataclass
from typing import List
from math import dist

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def find_the_best_shop(self, shops: List[Shop], fuel_price: float):
        shop_costs = {}
        for shop in shops:
            dist_ = dist(self.location, shop.location)
            one_way_cost = self.car.road_fuel_consumption(dist_) * fuel_price
            purchase_cost = sum(
                self.product_cart[product] * shop.products[product]
                for product in self.product_cart)
            total_cost = round(one_way_cost * 2 + purchase_cost, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            shop_costs[shop] = total_cost

        min_cost = min(cost for cost in list(shop_costs.values()))
        best_shop = None
        for key, value in list(shop_costs.items()):
            if value == min_cost:
                best_shop = key

        return best_shop, min_cost

    def perform_purchase(self, shops: List[Shop], fuel_price: float):
        print(f"{self.name} has {self.money} dollars")
        best_shop, cost = self.find_the_best_shop(shops, fuel_price)
        home_location = self.location
        if cost > self.money:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            print(f"{self.name} rides to {best_shop.name}\n")
            self.location = best_shop
            best_shop.form_purchase_receipt(self.name, self.product_cart)
            self.location = home_location
            self.money -= cost
            print(f"\n{self.name} rides home")
            print(f"{self.name} now has {self.money} dollars\n")
