from typing import Any

from app.customer import Customer
from app.shop import Shop

import json
import datetime


def shop_trip() -> Any:
    with open("app/config.json") as info_file:
        info = json.load(info_file)

    customers = [Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        customer["car"]["fuel_consumption"])
        for customer in info["customers"]]

    shops = [Shop(shop["name"], shop["location"], shop["products"])
             for shop in info["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        total_price = 1_000_000
        shop_to_go = None
        product_price = 0
        for shop in shops:
            coordinate_x = (customer.location[0] - shop.location[0]) ** 2
            coordinate_y = (customer.location[1] - shop.location[1]) ** 2
            distance = ((coordinate_x + coordinate_y) ** 0.5) * 2
            division = customer.fuel_consumption / 100
            fuel_for_trip = division * info["FUEL_PRICE"]
            distance_price = distance * fuel_for_trip

            price_for_products = 0
            for product in customer.products:
                customer_product = customer.products[product]
                shop_product = shop.products[product]
                price_for_products += customer_product * shop_product

            summary_cost = round(distance_price + price_for_products, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {summary_cost}")

            if summary_cost < total_price:
                total_price = summary_cost
                shop_to_go = shop
                product_price = price_for_products

        if total_price < customer.money:
            print(f"{customer.name} rides to {shop_to_go.name}\n")
            now_time = datetime.datetime.now()
            print(f"Date: {now_time.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            for product, amount in customer.products.items():
                print(
                    f"{amount} {product}s for "
                    f"{amount * shop_to_go.products[product]} dollars"
                )
            print(f"Total cost is {product_price} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.money -= total_price
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
