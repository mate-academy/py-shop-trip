import os


import datetime
import math


import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with (open(os.path.join(os.path.dirname(__file__), "config.json"))
          as config_json):
        config_data = json.load(config_json)
        customers = [
            Customer(**{**customer_data, "car": Car(**customer_data["car"])})
            for customer_data in config_data["customers"]
        ]

        shops = [Shop(**shop_data) for shop_data in config_data["shops"]]

        for customer in customers:

            def get_currency(amount: int | float) -> str:
                return "dollar" if float(amount) == 1.0 else "dollars"

            print(
                f"{customer.name} has {customer.money} "
                f"{get_currency(customer.money)}"
            )

            cheapest_store = [None, None, None]
            for shop in shops:
                ride_cost = (
                    math.dist(customer.location, shop.location)
                    * (customer.car.fuel_consumption / 100)
                    * config_data["FUEL_PRICE"]
                ) * 2
                products_cost = shop.get_price_of_cart(customer.product_cart)
                final_cost = round(ride_cost + products_cost["full_amount"], 2)

                print(
                    f"{customer.name}'s trip to "
                    f"the {shop.name} costs {final_cost}"
                )

                if cheapest_store[0] is not None:
                    if cheapest_store[0] > final_cost:
                        cheapest_store = [final_cost, shop, products_cost]
                else:
                    cheapest_store = [final_cost, shop, products_cost]

            if customer.money < cheapest_store[0]:
                print(
                    f"{customer.name} doesn't have enough"
                    f" money to make a purchase in any shop"
                )
            else:
                print(f"{customer.name} rides to {cheapest_store[1].name}")
                now = datetime.datetime.now()
                print("")
                time_formatted = now.strftime("%d/%m/%Y %H:%M:%S")
                print(f"Date: {time_formatted}")

                customer.money = round(customer.money - cheapest_store[0], 2)

                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought:")

                for (
                    product_name, price
                ) in cheapest_store[2]["detailed"].items():
                    print(
                        f"{customer.product_cart[product_name]} {product_name}"
                        f"s for {price} {get_currency(price)}"
                    )
                full_amount = cheapest_store[2]["full_amount"]
                print(
                    f"Total cost is {full_amount} "
                    f"{get_currency(cheapest_store[0])}"
                )
                print("See you again!")
                print("")

                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money} dollars")

                print("")
