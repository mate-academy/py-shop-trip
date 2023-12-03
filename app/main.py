import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as file:
        config = json.load(file)
        fuel_price = config["FUEL_PRICE"]

        shops = [Shop(fuel_price, **shop) for shop in config["shops"]]
        customers = [Customer(**customer) for customer in config["customers"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.find_cheapest_shop(shops)
        if customer.cheapest_shop is None:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        customer.make_a_purchase()
