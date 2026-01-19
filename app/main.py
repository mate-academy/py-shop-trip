import os
import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.getcwd(), "app", "config.json")
    with open(config_path) as file:
        info = json.load(file)

    fuel_price = info["FUEL_PRICE"]
    customers = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 customer["car"])
        for customer in info["customers"]
    ]
    shops = [
        Shop(shop["name"],
             shop["location"],
             shop["products"])
        for shop in info["shops"]]

    for customer in customers:
        print(f"{customer.client_name} has {customer.money} dollars")
        best_shop, best_cost = customer.right_store(shops, fuel_price)
        customer.trip_or_stay_home(best_shop, fuel_price)
