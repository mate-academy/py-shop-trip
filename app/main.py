import json
import sys
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    path = os.path.join("app", "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in data["shops"]]
    customers = [Customer(**customer) for customer in data["customers"]]

    for customer in customers:
        print(customer)

        cheapest_shop = None
        min_cost = sys.float_info.max

        for shop in shops:
            shopping_cost = customer.total_cost_calculation(shop, fuel_price)
            if shopping_cost < min_cost:
                min_cost = shopping_cost
                cheapest_shop = shop

        if customer.money >= min_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.shopping(cheapest_shop, min_cost)
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
