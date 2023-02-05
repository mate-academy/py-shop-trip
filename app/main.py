import json

from app.customer import Customers
from app.shops import Shops


def shop_trip():
    with open("config.json", "r") as data_file:
        config_file = json.load(data_file)
        for customer in config_file["customers"]:
            person = Customers(customer)
        for shop in config_file["shops"]:
            market = Shops(shop)
            print(market.name)
    return market


if __name__ == "__main__":
    print(shop_trip().list_of_shops)

