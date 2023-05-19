from __future__ import annotations

import json
import math
from datetime import datetime
from typing import Union

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config_file = json.load(file)

    customers_list = []
    shops_list = []
    fuel_price = config_file["FUEL_PRICE"]
    for customer in config_file["customers"]:
        customers_list.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"],
                ),
            )
        )
    for shop in config_file["shops"]:
        shops_list.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"],
            )
        )

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_prices: (Union[Shop | None], float) = (None, None)
        cheapest_shop_products = []
        for shop in shops_list:
            shop_dist = math.dist(customer.location, shop.location)
            cost_of_get_shop = (shop_dist * fuel_price
                                * customer.car.fuel_consumption / 100)
            cost_of_products = 0
            shop_products = []
            for product, value in customer.product_cart.items():
                cost_of_products += value * shop.products[product]
                shop_products.append(
                    [
                        product,
                        value,
                        value * shop.products[product]
                    ]
                )
            final_price = round(cost_of_get_shop * 2 + cost_of_products, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {final_price}")
            if cheapest_prices[0] is None or cheapest_prices[1] > final_price:
                cheapest_prices = (shop, final_price)
                cheapest_shop_products = shop_products

        if cheapest_prices[1] <= customer.money:
            print(f"{customer.name} rides to {cheapest_prices[0].name}\n")
            datetime_ = datetime(2021, 1, 4, 12, 33, 41)
            time_format = "%d/%m/%Y %H:%M:%S"
            print(f"Date: {str(datetime_.strftime(time_format))}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  f"You have bought: ")
            total_sum = 0
            for product in cheapest_shop_products:
                print(f"{product[1]} {product[0]}s for {product[2]} dollars")
                total_sum += product[2]
            print(f"Total cost is {total_sum} dollars\n"
                  f"See you again!\n\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has "
                  f"{round(customer.money - cheapest_prices[1], 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
