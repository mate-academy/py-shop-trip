import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r", encoding="utf-8") as file_obj:
        config = json.load(file_obj)

    fuel_price = float(config["FUEL_PRICE"])

    shops = []
    for shop_data in config["shops"]:
        shop_obj = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"],
        )
        shops.append(shop_obj)

    customers_data = config["customers"]

    for index, customer_data in enumerate(customers_data):
        if index > 0:
            print()

        car_data = customer_data["car"]
        car_obj = Car(car_data["brand"], car_data["fuel_consumption"])

        customer_obj = Customer(
            customer_data["name"],
            customer_data["location"],
            customer_data["money"],
            customer_data["product_cart"],
            car_obj,
        )

        print(f"{customer_obj.name} has {int(customer_obj.money)} dollars")

        trip_costs = []
        for shop_obj in shops:
            total_cost = customer_obj.evaluate_shop(shop_obj, fuel_price)
            if total_cost is None:
                continue

            print(
                f"{customer_obj.name}'s trip to the {shop_obj.name} "
                f"costs {total_cost:.2f}"
            )
            trip_costs.append((total_cost, shop_obj))

        affordable = [
            (cost, shop_obj)
            for cost, shop_obj in trip_costs
            if cost <= customer_obj.money
        ]
        if not affordable:
            print(
                f"{customer_obj.name} doesn't have enough money to make a "
                "purchase in any shop"
            )
            continue

        affordable.sort(key=lambda pair: pair[0])
        _, best_shop = affordable[0]

        print(f"{customer_obj.name} rides to {best_shop.name}")

        if customer_obj.go_to_shop(best_shop, fuel_price):
            print(f"{customer_obj.name} rides home")
            print(f"{customer_obj.name} now has {customer_obj.money:.2f} dollars")
