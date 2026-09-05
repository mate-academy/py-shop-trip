import json
import os

from app import customer, shop, car


def load_data() -> tuple[
    float | int,
    list[customer.Customer],
    list[shop.Shop]
]:
    path = os.path.join(str(os.path.dirname(__file__)), "config.json")
    with open(path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [
        customer.Customer(name=person["name"],
                          product_cart=person["product_cart"],
                          location=person["location"],
                          money=person["money"],
                          transport=car.Car(
                              person["car"]["brand"],
                              person["car"]["fuel_consumption"]))
        for person in data["customers"]
    ]
    shops = [
        shop.Shop(name=store["name"],
                  location=store["location"],
                  products=store["products"])
        for store in data["shops"]
    ]

    return fuel_price, customers, shops
