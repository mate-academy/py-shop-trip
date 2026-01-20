import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config = json.load(config)

    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(**customer)
        for customer in config["customers"]
    ]
    shops = [
        Shop(**shop)
        for shop in config["shops"]
    ]
    for customer in customers:
        customer.trip(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
