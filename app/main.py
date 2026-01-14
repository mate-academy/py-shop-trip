import json
import os

from .customer import Customer
from .car import Car
from .shop import Shop

base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, "config.json")


def shop_trip() -> None:
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    shop_list = []
    for shop in shops:
        shop_object = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shop_list.append(shop_object)

    for customer in customers:
        car_object = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        customer_object = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=car_object
        )

        print(f"{customer_object.name} has {customer_object.money} dollars")

        trips = customer_object.calculate_trips_to_all_shops(
            shop_list,
            fuel_price
        )

        for shop, cost in trips.items():
            print(
                f"{customer_object.name}'s trip to "
                f"the {shop.name} costs {cost}"
            )

        min_shop, min_cost_shop = customer_object.calculate_cheapest_trip(
            trips
        )

        if min_cost_shop > customer_object.money:
            print(
                f"{customer_object.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(f"{customer_object.name} rides to {min_shop.name}")
        customer_object.location = min_shop.location
        min_shop.print_receipt(
            customer_object.product_cart,
            customer_object.name
        )
        customer_object.update_money(min_cost_shop)
        customer_object.go_home()
