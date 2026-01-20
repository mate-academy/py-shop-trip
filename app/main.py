from __future__ import annotations

import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config_file = json.load(file)

    customers = [Customer.from_dict(customer)
                 for customer
                 in config_file["customers"]]
    shops = [Shop.from_dict(shop)
             for shop
             in config_file["shops"]]

    fuel_price = config_file["FUEL_PRICE"]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_to_go = customer.choose_shop(shops, fuel_price)
        if shop_to_go:
            print(f"{customer.name} rides to {shop_to_go.name}\n")
            shop_to_go.print_check(customer.name, customer.product_cart)
            customer.money -= customer.trip_to_shop_cost(
                shop_to_go,
                fuel_price
            )
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
