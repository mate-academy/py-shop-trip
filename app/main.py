import datetime
import json
import os

from .car import Car
from .customer import Customer
from .shop import Shop


def shop_trip() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(dir_path, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    customers = [
        Customer(c["name"],
                 c["product_cart"],
                 c["location"],
                 c["money"],
                 Car(c["car"]["brand"],
                     c["car"]["fuel_consumption"])
                 ) for c in config["customers"]
    ]
    shops = [
        Shop(s["name"],
             s["location"],
             s["products"])
        for s in config["shops"]
    ]
    datetime_now = datetime.datetime.now()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            print(
                f"{customer.name}'s trip to the"
                f" {shop.name}"
                f" costs {customer.calculate_trip_cost(shop)}"
            )
        chosen_shop, total_cost = customer.choose_shop(shops)
        if chosen_shop:
            print(f"{customer.name} rides to {chosen_shop.name}")
            customer.make_purchase(chosen_shop, datetime_now)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money to make a purchase in any shop")
            customer.location = customer.original_location
