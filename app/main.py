import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(
            s["name"],
            s["location"],
            s["products"]) for s in config["shops"]
    ]
    customers = [
        Customer(
            c["name"],
            c["product_cart"],
            c["location"],
            c["money"],
            c["car"]) for c in config["customers"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        min_cost = float("inf")
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            if trip_cost < min_cost:
                min_cost = trip_cost
                best_shop = shop
        if best_shop and customer.money >= min_cost:
            customer.perform_trip(best_shop, min_cost)
        else:
            print(
                f"{customer.name} doesn't have enough"
                f" money to make a purchase in any shop"
            )
