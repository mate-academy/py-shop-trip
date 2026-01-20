import json
import os
from typing import List, Dict, Any
from .customer import Customer
from .shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path, "r") as file:
        config: Dict[str, Any] = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    customers: List[Customer] = [
        Customer(**customer) for customer in config["customers"]
    ]
    shops: List[Shop] = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop: Shop = None
        cheapest_cost: float = float("inf")

        for shop in shops:
            trip_cost: float = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {trip_cost}")
            if trip_cost < cheapest_cost:
                cheapest_shop = shop
                cheapest_cost = trip_cost

        if cheapest_shop and customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.make_purchase(cheapest_shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
