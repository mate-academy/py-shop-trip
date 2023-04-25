import dataclasses
from typing import Dict, List
from app.car import Car
from app.shop import Shop, shops


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: Dict
    location: List[int]
    money: int
    car: Car
    enough_money: bool = False

    def calculate_trip_cost(self):
        products_cost = sum([cost for cost in self.product_cart.values()])
        return fuel_cost + products_cost

    def calculate_cost_to_get_shop(self, shop: Shop):
        distance_to_shop = self.calculate_distance(shop)
        fuel_cost = fuel_price * self.car.fuel_consumption * distance_to_shop / 100 * 2
        print(f"{self.name}'s trip to the {shop.name} Shop costs 28.21")
        return fuel_cost

    def pick_cheapest_trip(self, shops):
        return min([self.calculate_cost_to_get_shop(shop) for shop in shops])       # check if "[]" are needed, test

    def drives_to_shop(self, shop: Shop):
        ...
        self.location = shop.location

    def buys_products(self, shop: Shop):
        shop.print_receipt()

    def arrives_home(self):
        pass

    def counts_remaining_money(self):
        pass

    def calculate_distance(self, shop: Shop):
        return ...






customers = ...
