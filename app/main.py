import json
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json") as config:
        infos = json.load(config)

    fuel_price = infos["FUEL_PRICE"]

    customers_dict = {
        customer["name"]: Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]["fuel_consumption"]
        ) for customer in infos["customers"]
    }

    for customer in customers_dict.values():
        customer.cheapest_shop(fuel_price)
