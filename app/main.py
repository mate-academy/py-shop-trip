import datetime
import json
import math
from pathlib import Path


def _load_config():
    config_path = Path(__file__).resolve().parent / "config.json"
    with config_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def _calculate_trip_cost(customer, shop, fuel_price):
    customer_location = customer["location"]
    shop_location = shop["location"]

    distance = math.dist(customer_location, shop_location)
    round_trip_distance = distance * 2
    fuel_consumption = customer["car"]["fuel_consumption"]
    fuel_cost = (round_trip_distance / 100) * fuel_consumption * fuel_price

    product_total = sum(
        customer["product_cart"][product] * shop["products"][product]
        for product in customer["product_cart"]
    )

    total_cost = product_total + fuel_cost
    return product_total, round(total_cost + 1e-9, 2)


def _format_product_line(quantity, name, price):
    return f"{quantity} {name}s for {price:g} dollars"

def shop_trip():
    # write your code here
    config = _load_config()
    fuel_price = config["FUEL_PRICE"]
    now = datetime.datetime.now()

    for idx, customer in enumerate(config["customers"]):
        name = customer["name"]
        money = customer["money"]
        print(f"{name} has {money} dollars")

        shop_summaries = []
        for shop in config["shops"]:
            product_total, total_cost = _calculate_trip_cost(customer, shop, fuel_price)
            shop_summaries.append((shop, product_total, total_cost))
            print(f"{name}'s trip to the {shop['name']} costs {total_cost:.2f}")

        affordable_shops = [summary for summary in shop_summaries if summary[2] <= money]

        if not affordable_shops:
            print(f"{name} doesn't have enough money to make a purchase in any shop")
        else:
            best_shop, product_total, total_cost = min(
                affordable_shops, key=lambda summary: summary[2]
            )
            print(f"{name} rides to {best_shop['name']}")
            print()
            print(now.strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer["product_cart"].items():
                price = quantity * best_shop["products"][product]
                print(_format_product_line(quantity, product, price))

            print(f"Total cost is {product_total:g} dollars")
            print("See you again!")
            print()
            print(f"{name} rides home")
            remaining_money = money - total_cost
            print(f"{name} now has {remaining_money:.2f} dollars")

        if idx != len(config["customers"]) - 1:
            print()
