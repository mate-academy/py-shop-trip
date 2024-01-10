from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: List,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * 2
        return round(distance
                     * (fuel_price / 100)
                     * self.car.fuel_consumption, 2)

    def calculate_ful_cost(self, shop: Shop, fuel_price: float) -> float:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        purchase_cost = shop.calculate_purchase_cost(self)
        return round(trip_cost + purchase_cost, 2)

    def make_purchase(self, shops: List[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        min_costs = self.calculate_ful_cost(shops[0], fuel_price)
        min_shop = shops[0]
        for shop in shops:
            costs = self.calculate_ful_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {costs}")
            if costs < min_costs:
                min_costs = costs
                min_shop = shop
        if self.money < min_costs:
            print(f"{self.name} "
                  f"doesn't have enough money to make "
                  f"a purchase in any shop")
        else:
            print(f"{self.name} rides to {min_shop.name}\n")
            min_shop.print_receipt(self)
            self.money -= min_costs
            print(f"{self.name} rides home\n"
                  f"{self.name} now has {self.money} dollars\n")
