from __future__ import annotations

import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)
    fuel_price = config["FUEL_PRICE"]
    customers_config = config["customers"]
    shops_config = config["shops"]
    shops = [Shop(**shop_config) for shop_config in shops_config]
    customers = [
        Customer.from_dict(customer_config)
        for customer_config in customers_config
    ]
    for index, customer in enumerate(customers):
        if index > 0:
            print()
        print(f"{customer.name} has {customer.money} dollars")
        candidates = []
        for shop in shops:
            if not shop.has_products(customer.product_cart):
                continue

            trip_cost, product_costs, products_total = (
                customer.calculate_trip_cost(shop, fuel_price)
            )
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )
            candidates.append((trip_cost, shop, product_costs, products_total))

        if not candidates:
            print(f"{customer.name} could not find a shop with all products")
            continue

        trip_cost, shop, product_costs, products_total = min(
            candidates,
            key=lambda candidate: candidate[0],
        )

        if not customer.go_to_shop(shop, trip_cost):
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {shop.name}\n")

            shop.print_receipt(
                customer.product_cart,
                product_costs,
                products_total,
                customer.name,
            )

            print(f"{customer.name} rides home")
            customer.go_home()
            print(f"{customer.name} now has {customer.money:.2f} dollars")
