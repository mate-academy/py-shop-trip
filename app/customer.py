from math import sqrt
from typing import Generator

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.initial_location = location

    def get_distance_to_shop(self, shop: Shop) -> int | float:
        return sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )

    def calculate_min_ride_price(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> list:
        print(f"{self.name} has {self.money} dollars")
        prices = {}

        for shop in shops:
            one_km_consumption = self.car.one_km_consumption
            distance_to_shop = self.get_distance_to_shop(shop)
            fuel_amount = one_km_consumption * distance_to_shop
            ride_price = (fuel_amount * fuel_price) * 2

            products_price = sum(
                shop.products[product_name] * amount
                for product_name, amount in self.product_cart.items()
            )
            overall_price = round(ride_price + products_price, 2)

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {overall_price}"
            )
            prices[overall_price] = shop

        min_price = sorted(prices.keys())[0]
        shop = prices[min_price]

        return [shop, min_price]

    def visit_shop(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> None:
        shop, price = self.calculate_min_ride_price(shops, fuel_price)
        if self.money >= price:
            print(f"{self.name} rides to {shop.name}\n")
            shop.get_receipt(self.name, self.product_cart)
            self.go_home(price)
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

    def go_home(self, spent_money: int | float) -> None:
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money - spent_money} dollars\n"
        )
        self.location = self.initial_location


def create_customers(customers_dict: dict) -> Generator:
    return (
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                **customer["car"]
            )
        )
        for customer in customers_dict
    )
