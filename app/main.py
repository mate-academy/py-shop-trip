# main.py
import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json")) as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        customer.go_shopping(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
