import json

from app.customers import Customer
from app.shops import Shop
from app.expences import find_min_cost, print_receipt


def shop_trip() -> None:
    with open("app/config.json", "r") as data_json:
        data = json.load(data_json)
        fuel_price = data["FUEL_PRICE"]
    customer_instances = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ) for customer in data["customers"]
    ]
    shop_instances = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in data["shops"]
    ]

    for customer in customer_instances:
        expences_info = find_min_cost(customer, shop_instances, fuel_price)
        if expences_info:
            print_receipt(customer, expences_info)
