import json
import os

from app.utils import format_money
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(__file__)
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, encoding="utf-8") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"],
        )
        for shop_data in config["shops"]
    ]

    customers = []
    for data in config["customers"]:
        car = Car(
            data["car"]["brand"],
            data["car"]["fuel_consumption"],
        )
        customer = Customer(
            data["name"],
            data["product_cart"],
            data["location"],
            data["money"],
            car,
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {format_money(customer.money)} dollars")

        trip_costs = {}
        for shop in shops:
            total_cost = customer.total_trip_cost(shop, fuel_price)
            trip_costs[shop] = total_cost
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {format_money(total_cost)}"
            )

        cheapest_shop, cheapest_price = min(
            trip_costs.items(), key=lambda x: x[1]
        )

        if customer.money < cheapest_price:
            print(
                f"{customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")
        print()

        customer.go_to(cheapest_shop.location)

        cheapest_shop.print_receipt(customer)
        print()

        print(f"{customer.name} rides home")
        customer.go_home()

        customer.money -= cheapest_price
        print(
            f"{customer.name} now has "
            f"{format_money(customer.money)} dollars"
        )
        print()
