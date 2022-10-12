from __future__ import annotations
from json import load

from app.representation.representation import Representation
from app.data.shop import Shop
from app.data.customer import Customer


def shop_trip() -> None:

    with open("app/config.json") as file:
        data = load(file)

    representation = Representation(data["FUEL_PRICE"])

    customers = []
    for customer in data["customers"]:
        customers.append(Customer(**customer))

    shops = []
    for shop in data["shops"]:
        shops.append(Shop(**shop))

    for customer in customers:
        representation.print_info(customer, shops)
