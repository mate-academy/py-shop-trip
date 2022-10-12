from __future__ import annotations
from datetime import datetime

from app.data.shop import Shop
from app.data.customer import Customer


class Representation:

    def __init__(self, fuel_price: float | int) -> None:
        self.fuel_price = fuel_price

    def print_info(self, customer: Customer, shops: list[Shop]) -> None:
        print(f"{customer.name} has {customer.money} dollars")
        self._print_all_trips(customer, shops)
        self._make_purchases(customer, shops)

    def _print_all_trips(self, customer: Customer, shops: list[Shop]) -> None:
        for shop in shops:
            trip_cost = customer.trip_cost(shop, self.fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

    def _make_purchases(self, customer: Customer, shops: list[Shop]) -> None:
        selected_shop = min(shops, key=lambda shop:
                            customer.trip_cost(shop, self.fuel_price))

        if customer.money < customer.trip_cost(selected_shop, self.fuel_price):
            print(f"{customer.name} doesn't have enough money"
                  f" to make purchase in any shop")
            return

        print(f"{customer.name} rides to {selected_shop.name}")
        print()
        self._print_bought_products(customer, selected_shop)

    def _print_bought_products(self, customer: Customer, shop: Shop) -> None:
        date = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        product_cost = 0
        for name, count in customer.product_cart.items():
            print(f"{count} {name}s for {count * shop.products[name]} dollars")
            product_cost += count * shop.products[name]

        print(f"Total cost is {product_cost} dollars")
        print("See you again!")

        customer.money -= customer.trip_cost(shop, self.fuel_price)
        customer.money = round(customer.money, 2)

        print()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars")
        print()
