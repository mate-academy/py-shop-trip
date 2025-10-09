import datetime
import json
import math
from pathlib import Path
from typing import Any, Dict, Tuple


def _load_config() -> Dict[str, Any]:
    config_path = Path(__file__).resolve().parent / "config.json"
    with config_path.open("r", encoding="utf-8") as config_file:
        return json.load(config_file)


def _calculate_trip_cost(
    customer: Dict[str, Any],
    shop: Dict[str, Any],
    fuel_price: float,
) -> Tuple[float, float]:
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


def _format_money(value: float) -> str:
    return format(value, ".2f")


def _format_product_line(quantity: int, name: str, price: float) -> str:
    formatted_price = format(price, "g")
    return f"{quantity} {name}s for {formatted_price} dollars"


def _format_shop_trip_cost(
    name: str, shop_name: str, total_cost: float
) -> str:
    formatted_cost = _format_money(total_cost)
    return f"{name}'s trip to the {shop_name} costs {formatted_cost}"


def _format_insufficient_funds_message(name: str) -> str:
    return (
        f"{name} doesn't have enough money to make a purchase in any shop"
    )


def shop_trip() -> None:
    config = _load_config()
    fuel_price = config["FUEL_PRICE"]
    now = datetime.datetime.now()

    for idx, customer in enumerate(config["customers"]):
        name = customer["name"]
        money = customer["money"]
        print(f"{name} has {money} dollars")

        shop_summaries = []
        for shop in config["shops"]:
            product_total, total_cost = _calculate_trip_cost(
                customer, shop, fuel_price
            )
            shop_summaries.append((shop, product_total, total_cost))
            print(_format_shop_trip_cost(name, shop["name"], total_cost))

        affordable_shops = [
            summary for summary in shop_summaries if summary[2] <= money
        ]

        if not affordable_shops:
            print(_format_insufficient_funds_message(name))
        else:
            best_shop, product_total, total_cost = min(
                affordable_shops, key=lambda summary: summary[2]
            )
            best_shop_name = best_shop["name"]
            print(f"{name} rides to {best_shop_name}")
            print()
            print(now.strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer["product_cart"].items():
                price = quantity * best_shop["products"][product]
                print(_format_product_line(quantity, product, price))

            formatted_total = format(product_total, "g")
            print(f"Total cost is {formatted_total} dollars")
            print("See you again!")
            print()
            print(f"{name} rides home")
            remaining_money = money - total_cost
            formatted_balance = _format_money(remaining_money)
            print(f"{name} now has {formatted_balance} dollars")

        if idx != len(config["customers"]) - 1:
            print()
