from app.customer import Customer
from app.shop import Shop
from pathlib import Path
import json


def shop_trip() -> None:
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    with open(config_path, "r") as file:
        config = json.load(file)

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
            customer["car"]
        )
        for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(cost, 2)}")

            if cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if cheapest_cost <= customer.money:
            customer.visit_shop(cheapest_shop, fuel_price)
        else:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
