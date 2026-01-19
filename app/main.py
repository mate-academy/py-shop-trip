import os
from datetime import datetime
import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as config:
        config_data = json.load(config)
    fuel_prize = config_data["FUEL_PRICE"]

    list_customers = [Customer(customers["name"],
                               customers["product_cart"],
                               customers["location"],
                               customers["money"],
                               customers["car"]
                               ) for customers in config_data["customers"]]

    list_shops = [Shop(
        shops["name"],
        shops["location"],
        shops["products"])
        for shops in config_data["shops"]]

    for customer in list_customers:
        customer.customer_has_money()
        costs = float("inf")
        shop_obj = None
        for shop in list_shops:
            min_cost = (customer.cost_of_the_trip(
                fuel_prize,
                customer.location,
                shop.location) * 2 + shop.price_products(
                    customer.product_cart["milk"],
                    customer.product_cart["bread"],
                    customer.product_cart["butter"]
            ))
            if min_cost < costs:
                costs = min_cost
                shop_obj = shop
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {min_cost}")
        if customer.money < costs:
            customer.does_not_have_enough_money()

        else:
            customer.customer_ride_to_shop(shop_obj)
            now = datetime.now()
            print()
            print(now.strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            customer.bought_milk(shop_obj.products["milk"])
            customer.bought_bread(shop_obj.products["bread"])
            customer.bought_butter(shop_obj.products["butter"])
            total_cost = (customer.product_cart["milk"]
                          * shop_obj.products["milk"]
                          + customer.product_cart["bread"]
                          * shop_obj.products["bread"]
                          + customer.product_cart["butter"]
                          * shop_obj.products["butter"])
            print(f"Total cost is {total_cost} dollars")
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money - costs} dollars")
            print()
