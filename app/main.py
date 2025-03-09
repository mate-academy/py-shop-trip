import json

from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    for person in data["customers"]:
        customer = Customer(person)

        customer.trip(data["shops"], data["FUEL_PRICE"])
