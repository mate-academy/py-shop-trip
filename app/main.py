import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            trip_costs[shop] = cost
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")

        cheapest_shop = min(trip_costs, key=trip_costs.get)
        cheapest_cost = trip_costs[cheapest_shop]

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        customer.make_trip(cheapest_shop, cheapest_cost)
