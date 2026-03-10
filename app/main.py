import json
import os
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(s["name"], s["location"], s["products"])
        for s in config["shops"]
    ]

    customers = [
        Customer(
            c["name"],
            c["product_cart"],
            c["location"],
            c["money"],
            c["car"]
        )
        for c in config["customers"]
    ]

    for i, customer in enumerate(customers):
        money_str = f"{customer.money:.2f}".rstrip("0").rstrip(".")
        print(f"{customer.name} has {money_str} dollars")

        best_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost:.2f}"
            )

            if cost < min_cost:
                min_cost = cost
                best_shop = shop

        if best_shop and customer.money >= min_cost:
            print(f"{customer.name} rides to {best_shop.name}\n")

            customer.go_shopping(best_shop, min_cost)

            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough money to "
                f"make a purchase in any shop"
            )

        if i < len(customers) - 1:
            print()
