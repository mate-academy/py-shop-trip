import json
import os

from app.customer import Customer


def shop_trip() -> None:
    current_dir = os.path.dirname(__file__)
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    customers_data = config["customers"]
    shops = config["shops"]
    fuel_price = config["FUEL_PRICE"]

    customers = [Customer(
        customer, shops, fuel_price) for customer in customers_data]
    for customer in customers:
        print(customer.generate_trip_summary())


if __name__ == "__main__":
    shop_trip()
