from __future__ import annotations
from math import dist
import datetime
from decimal import Decimal

from app.car import Car
from app.shop import Shop
from app.products import Products


class Customer:
    customers = []
    fuel_price: Decimal = 0

    def __init__(self,
                 name: str,
                 product_cart: Products,
                 location: list,
                 money: Decimal,
                 car: Car
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        Customer.customers.append(self)

    def get_product_cost(self, shop: Shop) -> Decimal:
        product_cost = (
            self.product_cart.milk * shop.products.milk
            + self.product_cart.bread * shop.products.bread
            + self.product_cart.butter * shop.products.butter
        )
        return product_cost

    def get_journey_cost(self, shop: Shop) -> Decimal:
        distance = Decimal(dist(shop.location, self.location))
        return distance * self.car.fuel_consumption * Customer.fuel_price / 100

    def get_trip_to_cost(self, shop: Shop) -> Decimal:
        trip_cost = self.get_journey_cost(shop)
        products_cost = self.get_product_cost(shop)
        trip_cost = 2 * trip_cost + products_cost
        return trip_cost.quantize(Decimal("0.00"))

    def check_trip_availability(self) -> str:
        print(f"{self.name} has "
              f"{self.money.quantize(Decimal('0.00'))} dollars")
        trip_cost = {}
        for shop in Shop.shops:
            cost = self.get_trip_to_cost(shop)
            trip_cost[shop.name] = cost
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

        min_value = min([value for key, value in trip_cost.items()])
        chosen_shop_name = [key
                            for key in trip_cost.keys()
                            if trip_cost[key] == min_value
                            ][0]
        chosen_shop = [shop
                       for shop in Shop.shops
                       if shop.name == chosen_shop_name
                       ][0]

        if self.money >= min_value:
            print(f"{self.name} rides to {chosen_shop.name}\n")
            self.money -= self.get_trip_to_cost(chosen_shop)
            self.location = chosen_shop.location
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            chosen_shop = None
        return chosen_shop

    def get_receipt(self, shop: Shop) -> None:
        date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_milk_price = shop.products.milk * self.product_cart.milk
        total_bread_price = shop.products.bread * self.product_cart.bread
        total_butter_price = shop.products.butter * self.product_cart.butter
        print(f"{self.product_cart.milk} milks "
              f"for {total_milk_price.quantize(Decimal('0.00'))} dollars")
        print(f"{self.product_cart.bread} breads "
              f"for {total_bread_price.quantize(Decimal('0.00'))} dollars")
        print(f"{self.product_cart.butter} butters "
              f"for {total_butter_price.quantize(Decimal('0.00'))} dollars")
        print(f"Total cost is "
              f"{self.get_product_cost(shop).quantize(Decimal('0.00'))} "
              f"dollars")
        print("See you again!\n")

    def arrive_home(self) -> None:
        if self.money >= 0:
            print(f"{self.name} rides home")
            print(f"{self.name} now has "
                  f"{self.money.quantize(Decimal('0.00'))} dollars\n")
