import json
import os
from app.cost_calculation import CostCalculation
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = {}
    shops = {}
    print()
    source = os.path.join(os.path.dirname(__file__), "config.json")
    data = None

    with open(source, "r") as file:
        data = json.load(file)

    for customer in data["customers"]:
        customers[customer["name"]] = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=customer["car"]
        )

    for shop in data["shops"]:
        shops[shop["name"]] = Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )

    CostCalculation(
        customers, shops, data["FUEL_PRICE"]
    ).calculation()
