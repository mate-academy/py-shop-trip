import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)

    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        customer.determine_cheapest_shop_and_visit_it(
            shops=shops,
            fuel_price=data["FUEL_PRICE"]
        )
