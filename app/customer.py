import math
import datetime
from typing import Type
from app.shop import Shop


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]
        self.best_shop = None
        self.best_shop_products_cost = None
        self.best_shop_shopping_cost = None

    def find_best_shop(self, list_of_shops: list, fuel_price: float) -> None:
        for shop in list_of_shops:
            fuel_price_per_trip = \
                self.find_fuel_price_to_each_shop(shop, fuel_price)

            products_cost = self.find_product_cart_price(shop)
            shopping_cost = fuel_price_per_trip + products_cost
            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{round(shopping_cost, 2)}")
            if self.best_shop is None or \
                    shopping_cost < self.best_shop_shopping_cost:
                self.best_shop = shop
                self.best_shop_products_cost = products_cost
                self.best_shop_shopping_cost = shopping_cost

        if self.money < self.best_shop_shopping_cost:
            print(f"{self.name} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            print(f"{self.name} rides to {self.best_shop.name}\n")
            self.print_check(self.best_shop)

    def find_fuel_price_to_each_shop(
            self,
            shop: Type[Shop],
            fuel_price: float
    ) -> float:

        trip_road_distance = math.dist(self.location,
                                       shop.location) * 2
        one_km_cost = self.car["fuel_consumption"] * fuel_price / 100
        fuel_price_per_trip = trip_road_distance * one_km_cost

        return round(fuel_price_per_trip, 2)

    def find_product_cart_price(self, shop: Type[Shop]) -> float:
        all_products_price = 0
        for product_name, product_amount in self.product_cart.items():
            all_products_price += shop.products[product_name] * product_amount
        return all_products_price

    def print_check(self, shop: Type[Shop]) -> None:
        current_time = datetime.datetime.now()
        print(f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        product_cost = 0
        for (product_name, product_amount)\
                in self.product_cart.items():
            price_for_one_product_set = round(
                (self.product_cart[product_name]
                 * shop.products[product_name]), 2)
            print(f"{product_amount} {product_name}s for "
                  f"{price_for_one_product_set} dollars")
            product_cost += price_for_one_product_set
        print(f"Total cost is {product_cost} dollars")
        print("See you again!\n")
        self.returning_home()

    def returning_home(self) -> None:
        print(f"{self.name} rides home")
        money_left = round((self.money - self.best_shop_shopping_cost), 2)
        print(f"{self.name} now has {money_left} dollars\n")
