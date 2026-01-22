import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_path = os.path.dirname(__file__)
    config_path = os.path.join(base_path, "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**s) for s in config["shops"]]
    customers = [Customer(**c) for c in config["customers"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        min_total_cost = float("inf")

        for shop in shops:
            total_cost = customer.get_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost:.2f}")
            if total_cost < min_total_cost:
                min_total_cost = total_cost
                best_shop = shop

        if best_shop and min_total_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.location = best_shop.location
            best_shop.print_receipt(customer.name, customer.product_cart)
            customer.money -= min_total_cost
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  "purchase in any shop\n")
