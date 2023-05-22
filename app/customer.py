from __future__ import annotations
import math
import datetime

from typing import List
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def create_customers(customers_data: dict) -> List[Customer]:
        customers_json = customers_data["customers"]
        Car.fuel_price = customers_data["FUEL_PRICE"]
        customers = [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
            )
            for customer in customers_json
        ]
        return customers

    def calculate_distance(self, shop: Shop) -> float:
        customer_x_coord, customer_y_coord = self.location
        shop_x_coord, shop_y_coord = shop.location
        distance = math.sqrt((shop_x_coord - customer_x_coord) ** 2
                             + (shop_y_coord - customer_y_coord) ** 2)
        return distance

    def calculate_products_price(self, shop: Shop) -> float:
        price = 0
        for item in self.product_cart:
            number_of_products = self.product_cart[item]
            price_of_products = shop.products[item]
            final_price = number_of_products * price_of_products
            price += final_price
        return price

    def calculate_distance_price(self,
                                 shop: Shop) -> float:
        fuel_used = ((self.car.fuel_consumption / 100)
                     * self.calculate_distance(shop))
        return Car.fuel_price * fuel_used * 2

    def calculate_total_price(self, shop: Shop) -> float:
        return round((self.calculate_products_price(shop)
                      + self.calculate_distance_price(shop)), 2)

    def visit_shop(self, shop: Shop) -> None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime(
            "Date: %d/%m/%Y %H:%M:%S"
        )
        print(formatted_datetime)
        final_price = 0
        print(f"Thanks, {self}, for your purchase!\nYou have bought: ")
        for product, quantity in self.product_cart.items():
            price = quantity * shop.products[product]
            final_price += price
            print(f"{quantity} {product}s for {price} dollars")
        print(f"Total cost is {final_price} dollars\nSee you again!\n")

    def select_cheapest_shop(self, shops: List[Shop]) -> Shop:
        best_price = float("inf")
        best_shop = shops[0]
        self.ask_money()
        for shop in shops:
            price = self.calculate_total_price(shop)
            print(f"{self}'s trip to the {shop} costs {price}")
            if price < best_price:
                best_price = price
                best_shop = shop
        if self.money >= best_price:
            print(f"{self} rides to {best_shop}\n")
            self.visit_shop(best_shop)
            self.money -= best_price
            print(f"{self} rides home\n{self} now has {self.money} dollars\n")
        else:
            print((f"{self} doesn't have enough money "
                   f"to make a purchase in any shop"))
        return best_shop

    def ask_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def __repr__(self) -> str:
        return f"{self.name}, {self.money} dollars"

    def __str__(self) -> str:
        return self.name
