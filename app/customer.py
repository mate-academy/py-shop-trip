from __future__ import annotations
from datetime import datetime
from app.location import Location
from app.car import Car
from app.shop import Shop


class Customer:
    fuel_price = None

    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = Location(location)
        self.money = money
        self.car = Car(**car)

    @classmethod
    def from_dict(cls, info: dict) -> Customer:
        return cls(**info)

    @staticmethod
    def get_date() -> None:
        time_now = datetime(2021, 1, 4, 12, 33, 41)
        time_now_formatted = time_now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_now_formatted}")

    def get_fuel_cost(self, shop: Shop) -> float:
        fuel = self.car.get_fuel(self.location, shop.location)
        money = 2 * fuel * self.fuel_price
        return money

    def get_food_cost(self, shop: Shop) -> float:
        food_cost = sum(
            quantity * shop.products.get(name)
            for name, quantity in self.product_cart.items()
        )
        return food_cost

    def cost_calculator(self, shop: Shop) -> tuple:
        fuel_cost = self.get_fuel_cost(shop)
        food_cost = shop.get_food_cost(self.product_cart)
        total_cost = round(fuel_cost + food_cost, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        return total_cost, shop

    def buy_at_shop(self, shop: Shop) -> None:
        self.get_date()
        print(f"Thanks, {self.name}, for you purchase!\nYou have bought: ")
        for name, quantity in self.product_cart.items():
            print(f"{quantity} {name}s for "
                  f"{shop.products.get(name) * quantity} dollars")
        product_cost = self.get_food_cost(shop)
        print(f"Total cost is {product_cost} dollars\nSee you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def choose_shop(self, shops: list[Shop]) -> Shop | None:
        print(f"{self.name} has {self.money} dollars")
        cost, shop = min(
            [self.cost_calculator(shop) for shop in shops], key=lambda x: x[0]
        )
        if cost <= self.money:
            print(f"{self.name} rides to {shop.name}\n")
            self.money = round(self.money - cost, 2)
            return shop
        print(
            f"{self.name} doesn't have enough"
            f" money to make purchase in any shop"
        )
