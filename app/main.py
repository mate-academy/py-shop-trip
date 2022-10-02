from __future__ import annotations
import json
from app.customer import Customer
from app.shop import Shop


def open_file() -> tuple[list[Customer], list[Shop], float]:
    with open("app/config.json") as f:
        data = json.load(f)
        fuel_price = data["FUEL_PRICE"]
    customers_list = [Customer(customer) for customer in data["customers"]]
    shops_list = [Shop(shop) for shop in data["shops"]]
    return customers_list, shops_list, fuel_price


def shop_trip() -> None:
    customers, shops, fuel = open_file()
    for customer in customers:
        customer.trip_to_shop(shops, fuel)


if __name__ == "__main__":
    shop_trip()
