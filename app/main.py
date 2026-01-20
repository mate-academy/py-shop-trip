import json

from pathlib import Path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent.joinpath("config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

        fuel_price = config.get("FUEL_PRICE")

        customers = [
            Customer.from_dict(customer)
            for customer in config.get("customers")
        ]

        shops = [
            Shop.from_dict(shop)
            for shop in config.get("shops")
        ]

    for customer in customers:
        customer.make_purchases(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
