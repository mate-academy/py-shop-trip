from typing import List

import datetime
import math

from app.shop import Shop
from app.car import Car


class Customer:

    def __init__(self, customer_dictionary: dict) -> None:
        self.name = customer_dictionary.get("name")
        self.product_cart = customer_dictionary.get("product_cart")
        self.location = customer_dictionary.get("location")
        self.money = customer_dictionary.get("money")
        self.car = Car(customer_dictionary.get("car"))

    def distance_to_the_shop(self, shop: Shop) -> float:
        return math.sqrt((self.location[0] - shop.location[0]) ** 2
                         + (self.location[1] - shop.location[1]) ** 2)

    def count_product_cart_price(self, shop: Shop) -> float:
        return sum(
            amount * shop.products[product]
            for product, amount
            in self.product_cart.items()
        )

    def ride_to_shop_price(self, fuel_price: float, shop: Shop) -> float:
        return (round(self.distance_to_the_shop(shop) * 2
                      * self.car.fuel_consumption / 100
                      * fuel_price, 2) + self.count_product_cart_price(shop))

    def print_receipt(self, shop: Shop) -> None:
        receipt = (f"\nDate: "
                   f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                   f"\nThanks, {self.name}, for your purchase!"
                   f"\nYou have bought: ")
        for product, amount in self.product_cart.items():
            receipt += (f"\n{amount} {product}s"
                        f" for {amount * shop.products[product]}"
                        f" dollars")

        receipt += (f"\nTotal cost is {self.count_product_cart_price(shop)}"
                    f" dollars\nSee you again!\n")
        print(receipt)

    def go_shopping(self,
                    fuel_price: float,
                    shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        min_price_shop = None
        min_price = self.ride_to_shop_price(fuel_price, shops[0])
        for shop in shops:
            ride_to_shop_price = self.ride_to_shop_price(fuel_price, shop)
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {ride_to_shop_price}")
            if min_price >= ride_to_shop_price:
                min_price = ride_to_shop_price
                min_price_shop = shop

        if self.money >= min_price:
            home_location = self.location
            print(f"{self.name} rides to {min_price_shop.name}")
            self.location = min_price_shop.location
            self.print_receipt(min_price_shop)
            print(f"{self.name} rides home")
            self.location = home_location
            self.money -= min_price
            print(f"{self.name} now has {self.money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money to"
                  f" make a purchase in any shop")

    def __repr__(self) -> str:
        return (
            f"\nName: {self.name},"
            f"Money: {self.money},"
            f"Location: {self.location},"
            f"Product cart: {self.product_cart},"
            f"Car: {self.car}."
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def product_cart(self) -> dict:
        return self._product_cart

    @property
    def location(self) -> list:
        return self._location

    @property
    def money(self) -> int:
        return self._money

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Name should be a string!")
        self._name = new_name

    @product_cart.setter
    def product_cart(self, new_products: dict) -> None:
        if not isinstance(new_products, dict):
            raise TypeError("Products should be in list")
        if not all(isinstance(key, str) for key in new_products.keys()):
            raise TypeError("Keys in product list should be strings")
        if not all(isinstance(value, int)
                   or isinstance(value, float)
                   for value in new_products.values()):
            raise TypeError("Values in product list should be numeric")
        if any(value < 0 for value in new_products.values()):
            raise ValueError("Values in product list should be positive")
        self._product_cart = new_products

    @location.setter
    def location(self, new_location: List[int]) -> None:
        if not isinstance(new_location, list):
            raise TypeError("Location should be a list!")
        if not len(new_location) == 2:
            raise ValueError("Location should contain only 2 coordinates!")
        if not all(isinstance(elem, int) for elem in new_location):
            raise ValueError("Coordinates should be integers!")
        self._location = new_location

    @money.setter
    def money(self, new_value: float | int) -> None:
        if not (isinstance(new_value, int) or isinstance(new_value, float)):
            raise TypeError("Money should be numeric")
        if new_value < 0:
            raise ValueError("Money should be positive")
        self._money = new_value
