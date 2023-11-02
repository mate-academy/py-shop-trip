import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data.get("FUEL_PRICE")

    customers = [
        Customer(**customer)
        for customer in data.get("customers")
    ]

    shops = [Shop(**shop) for shop in data.get("shops")]

    for customer in customers:
        customer.print_trip(fuel_price, shops)
