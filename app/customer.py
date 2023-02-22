from decimal import Decimal
from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def find_optimal_shop(self, shops: List[Shop], fuel_price: float) -> list:
        print(f"{self.name} has {self.money} dollars")
        optimal_shop = [shops[0], "", 10 ** 6]
        for shop in shops:
            total_cost = self.calculate_the_cost_to_the_shop(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            if total_cost < optimal_shop[2]:
                optimal_shop = [shop, shop.name, total_cost]
        return optimal_shop

    def has_enough_money(self, optimal_shop: list) -> None:
        print(f"{self.name} rides to {optimal_shop[1]}")
        self.location = optimal_shop[0].location
        print()

        self.print_check_of_customer(optimal_shop[0])
        print()

        print(f"{self.name} rides home")
        self.location = self.home_location
        current_wallet = self.money - optimal_shop[2]
        print(f"{self.name} now has {current_wallet} dollars")
        print()

    def has_not_enough_money(self) -> None:
        print(f"{self.name} "
              f"doesn't have enough money to make purchase in any shop")

    def calculate_the_cost_to_the_shop(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        distance_x = shop.location[0] - self.location[0]
        distance_y = shop.location[1] - self.location[1]
        distance_to_shop = (distance_x ** 2 + distance_y ** 2) ** (1 / 2)
        cost_of_road = Decimal(distance_to_shop * (self.car.fuel_consumption
                                                   / 100) * fuel_price) * 2

        cost_of_products = 0
        for key, value in self.product_cart.items():
            cost_of_products += (shop.products[key] * value)

        return round(cost_of_road + Decimal(cost_of_products), 2)

    def print_check_of_customer(self, shop: Shop) -> None:
        print("Date: 04/01/2021 12:33:41")

        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for key, value in self.product_cart.items():
            print(f"{value} {key}s for {shop.products[key] * value} dollars")
            total_cost += (shop.products[key] * value)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
