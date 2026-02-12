import json
import os
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    fuel_price = config["FUEL_PRICE"]
    shops_data = config["shops"]
    customers_data = config["customers"]
    shops = []
    for sho in shops_data:
        shop = Shop(sho["name"], sho["location"], sho["products"])
        shops.append(shop)

    for idx, ca in enumerate(customers_data):
        if idx != 0:
            print()

        car = Car(ca["car"]["brand"], ca["car"]["fuel_consumption"])
        customer = Customer(
            ca["name"],
            ca["location"],
            ca["money"],
            ca["product_cart"],
            car
        )

        print(f"{customer.name} has {int(customer.money)} dollars")

        costs = []
        for shop in shops:
            cost = customer.evaluate_shop(shop, fuel_price)
            if cost is None:
                continue
            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}"
            )
            costs.append((cost, shop))

        affordable = [
            (cost, shop)for cost, shop in costs if cost <= customer.money
        ]
        if not affordable:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            continue

        affordable.sort(key=lambda x: x[0])
        best_cost, best_shop = affordable[0]
        print(f"{customer.name} rides to {best_shop.name}")

        success = customer.go_to_shop(best_shop, fuel_price)
        if success:
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")


if __name__ == "__main__":
    shop_trip()
