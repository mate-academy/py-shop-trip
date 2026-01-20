import math
from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car

    def calculate_products_cost(self, shop: Shop,
                                print_info: bool = False) -> float:
        product_cost = sum([shop.products[key] * self.product_cart[key] for key
                            in self.product_cart])
        if print_info:
            date = datetime(2021, 1, 4, 12, 33, 41)
            date_str = date.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date_str}\n"
                  f"Thanks, {self.name}, for your purchase!\n"
                  "You have bought:")
            for key, value in self.product_cart.items():
                price = shop.products[key] * value
                if price % 1 == 0:
                    price = int(price)
                print(f"{value} {key}s for {price} dollars")
            print(f"Total cost is {product_cost} dollars\n"
                  "See you again!\n")

        return product_cost

    def calculate_travel_expenses(self, shop: Shop,
                                  fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        return (distance * 2 * self.car.fuel_consumption / 100) * fuel_price

    def calculate_shops_trip(self, shops: List[Shop],
                             fuel_price: float) -> dict:
        shops_dict = {}
        for shop in shops:
            products = self.calculate_products_cost(shop)
            trip = self.calculate_travel_expenses(shop, fuel_price)
            shops_dict[shop.name] = round(products + trip, 2)
        return shops_dict

    def print_info(self, shops: List[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        shops_trip = self.calculate_shops_trip(shops, fuel_price)
        for key, value in shops_trip.items():
            print(f"{self.name}'s trip to the {key} costs {value}")

        selected_shop_name = min(shops_trip, key=shops_trip.get)
        selected_shop_expenses = shops_trip[selected_shop_name]
        if self.money >= shops_trip[selected_shop_name]:
            print(f"{self.name} rides to {selected_shop_name}\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        selected_shop_instance = None
        for shop in shops:
            if shop.name == selected_shop_name:
                selected_shop_instance = shop
        self.calculate_products_cost(selected_shop_instance, print_info=True)

        print(f"{self.name} rides home\n"
              f"{self.name} now has "
              f"{self.money - selected_shop_expenses} dollars\n")
