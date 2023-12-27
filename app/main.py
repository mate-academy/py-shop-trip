import datetime
import math
import os
import json
from typing import Any, Dict

from app.customers import Customers
from app.shop import Shop


def load_config_data() -> Dict[str, Any]:
    folder = "app"
    file_name = "config.json"
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(project_path, folder, file_name)
    with open(file_path, "r") as config_file:
        return json.load(config_file)


def calculation_distance_and_cost(
        customer: Customers,
        shop: Shop) -> tuple[float, Any]:
    x1, y1 = customer.location
    x2, y2 = shop.location
    distance_to_shop = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    fuel_cost_to_shop = (
        (distance_to_shop / 100)
        * customer.fuel_consumption
        * customer.fuel_price
    )

    products_cost = sum(
        shop.products.get(product, 0) * quantity
        for product, quantity in customer.product_cart.items()
    )

    """back home"""
    distance_to_home = distance_to_shop
    fuel_cost_to_home = (
        (distance_to_home / 100)
        * customer.fuel_consumption
        * customer.fuel_price
    )

    total_cost = (round(
        fuel_cost_to_shop
        + products_cost
        + fuel_cost_to_home, 2)
    )

    return distance_to_shop, total_cost


def shop_trip() -> None:
    config_data = load_config_data()

    customer_data = config_data["customers"]
    shop_data = config_data["shops"]
    fuel_price = config_data["FUEL_PRICE"]

    customers = Customers.load_person(customer_data, fuel_price)
    shops = Shop.get_shops(shop_data)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_distance = None
        cheapest_store = None

        for shop in shops:
            distance, total_cost = (
                calculation_distance_and_cost(customer, shop)
            )

            print(
                f"{customer.name}'s "
                f"" f"trip to the {shop.name} " f"costs {total_cost}"
            )

            if cheapest_distance is None or total_cost < cheapest_distance:
                cheapest_distance = total_cost
                cheapest_store = shop

        if customer.money >= cheapest_distance:
            customer.location = cheapest_store.location
            print(f"{customer.name} rides to {cheapest_store.name}\n")

            receipt = cheapest_store.purchase(
                customer,
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(receipt)

            customer.money -= cheapest_distance
            print(f"\n{customer.name} rides home")
            print(
                f"{customer.name} now has {round(customer.money, 2)} dollars"
            )
            print()
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
