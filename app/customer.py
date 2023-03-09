import dataclasses

from math import sqrt
from typing import Tuple

from app.shop import Shop
from app.car import Car


@dataclasses.dataclass
class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: Tuple[int, int],
            money: float,
            car: Car
    ) -> None:
        self.__name = name
        self.__product_cart = product_cart
        self.__location = location
        self.__money = money
        self.__car = car

    @property
    def name(self) -> str:
        return self.__name

    @property
    def product_cart(self) -> dict:
        return self.__product_cart

    @product_cart.setter
    def product_cart(self, value: dict) -> None:
        self.__product_cart = value

    @property
    def location(self) -> list:
        return self.__location

    @location.setter
    def location(self, value: list) -> None:
        self.__location = value

    @property
    def money(self) -> float:
        return self.__money

    @money.setter
    def money(self, value: float) -> None:
        self.__money = value

    @property
    def car(self) -> Car:
        return self.__car

    def get_distance_to_the_shop(self, shop: Shop) -> float:
        return sqrt(
            (
                shop.location[0] - self.location[0]
            ) ** 2 + (
                shop.location[1] - self.location[1]
            ) ** 2
        )

    def cost_of_the_trip(self, shop: Shop, fuel_price: float) -> float:
        money_for_all_products = sum(
            [
                amount * shop.products[product]
                for product, amount in self.product_cart.items()
            ]
        )
        money_for_fuel = 2 * (
            (
                self.get_distance_to_the_shop(shop)
            ) * fuel_price * self.car.fuel_consumption / 100
        )
        return money_for_fuel + money_for_all_products

    def go_to_the_shop(self, shop: Shop) -> None:
        if self.money >= self.cost_of_the_trip(shop, self.car.fuel_price):
            print(f"{self.name} rides to {shop.name}\n")
            shop.buy_products(self.product_cart, self.name)
            print(f"{self.name} rides home")
            self.money -= self.cost_of_the_trip(shop, self.car.fuel_price)
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
