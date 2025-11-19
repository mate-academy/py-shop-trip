import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.utils import format_number


def shop_trip() -> None:
    module_dir = os.path.dirname(__file__)
    config_path = os.path.join(module_dir, "config.json")
    with open(config_path) as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_cost = None
        best_shop = None
        for shop in shops:
            trip_cost = customer.trip_cost(shop.location, fuel_price) * 2 \
                + shop.purchase_cost(customer.product_cart)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {format_number(trip_cost)}")

            if min_cost is None or trip_cost < min_cost:
                min_cost = trip_cost
                best_shop = shop

        if min_cost is not None:
            if customer.money >= min_cost:
                print(f"{customer.name} rides to {best_shop.name}\n")
                customer.move(best_shop.location)
                best_shop.proceed_purchase(
                    customer.name, customer.product_cart
                )
                print(f"\n{customer.name} rides home")
                customer.money -= min_cost
                print(f"{customer.name} now has"
                      f" {format_number(customer.money)} dollars\n")
            else:
                print(f"{customer.name} doesn't have enough "
                      f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
