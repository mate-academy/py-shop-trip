import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = float(config["FUEL_PRICE"])

    shops = []
    for s in config["shops"]:
        shops.append(Shop(s["name"], s["location"], s["products"]))

    customers_data = config["customers"]

    for idx, c in enumerate(customers_data):
        if idx > 0:
            print()

        car_data = c["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customer = Customer(
            c["name"],
            c["location"],
            c["money"],
            c["product_cart"],
            car,
        )

        print(f"{customer.name} has {int(customer.money)} dollars")

        costs = []
        for shop in shops:
            cost = customer.evaluate_shop(shop, fuel_price)
            if cost is None:
                continue
            print(f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}")
            costs.append((cost, shop))

        affordable = [(cost, shop) for cost, shop in costs if cost <= customer.money]
        if not affordable:
            print(
                f"{customer.name} doesn't have enough money to make a purchase in any "
                "shop"
            )
            continue

        affordable.sort(key=lambda x: x[0])
        _, best_shop = affordable[0]

        print(f"{customer.name} rides to {best_shop.name}")

        success = customer.go_to_shop(best_shop, fuel_price)
        if success:
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")

    shop_trip()
