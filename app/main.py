import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

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

    shops = [
        Shop(
            s["name"],
            s["location"],
            s["products"]
        )
        for s in config["shops"]
    ]

    for i, customer in enumerate(customers):
        money_str = int(customer.money) \
            if customer.money % 1 == 0 \
            else round(customer.money, 2)
        print(f"{customer.name} has {money_str} dollars")

        cheapest_shop = None
        lowest_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {cost:.2f}")

            if cost < lowest_cost:
                lowest_cost = cost
                cheapest_shop = shop

        if customer.money >= lowest_cost:
            customer.perform_trip(cheapest_shop, lowest_cost)
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money "
                  f"to make a purchase in any shop")

        if i < len(customers) - 1:
            print()


if __name__ == "__main__":
    shop_trip()
