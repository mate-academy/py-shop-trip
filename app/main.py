import json
import os

from app.customer import Customer
from app.shop import Shop


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def shop_trip() -> None:
    config_path = os.path.join(BASE_DIR, "config.json")

    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer.from_dict(customers_info)
        for customers_info in config["customers"]]
    shops = [
        Shop.from_dict(shops_info)
        for shops_info in config["shops"]]

    for customer in customers:
        customer.trip_info(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
