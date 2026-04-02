import json
from typing import Any, Dict, List
import os
from app.customer import Customer
from app.shop import Shop, format_money  # import format_money


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path, "r") as file:
        config: Dict[str, Any] = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    shops: List[Shop] = [
        Shop(s["name"], s["location"], s["products"])
        for s in config["shops"]
    ]
    customers: List[Customer] = [Customer(c) for c in config["customers"]]

    for customer in customers:
        money_str = format_money(customer.money)
        print(f"{customer.name} has {money_str} dollars")

        shop = customer.choose_shop(shops, fuel_price)

        if shop:
            customer.ride_and_buy(shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
