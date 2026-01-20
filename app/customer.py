from math import dist
from typing import List
from app.shop import Shop


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name: str = customer["name"]
        self.product_cart: dict = customer["product_cart"]
        self.location: List[int] = customer["location"]
        self.money: int = customer["money"]
        self.car: dict = customer["car"]

    def get_fuel_cost(self,
                      fuel_price: float,
                      shop_location: List[int]) -> float:
        distance = dist(self.location, shop_location)
        return self.car["fuel_consumption"] * distance / 100 * fuel_price

    def get_product_cost(self, product_shop: dict) -> float:
        return sum(
            product_shop[product] * cost
            for product, cost in self.product_cart.items()
        )

    def find_cheap_shop(self, fuel_price: float, shops: List[Shop]) -> tuple:
        print(f"{self.name} has {self.money} dollars")
        cheap_shop_price = {}
        for shop in shops:
            fuel_cost = self.get_fuel_cost(fuel_price, shop.location) * 2
            product_price = self.get_product_cost(shop.product)
            total_cost = round((fuel_cost + product_price), 2)
            cheap_shop_price[total_cost] = shop
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        min_price = min(cheap_shop_price)
        return cheap_shop_price[min_price], min_price

    def left_money_after_shopping(self,
                                  shop: Shop,
                                  fuel_price: float,
                                  product_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        fuel_cost = self.get_fuel_cost(fuel_price, shop.location) * 2
        self.money -= fuel_cost
        self.money -= product_cost

    def way_home(self) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")
