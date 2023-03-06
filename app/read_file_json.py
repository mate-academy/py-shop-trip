from json import load

from app.customer import Customer
from app.shop import Shop


def read_json() -> tuple:
    with open("app/config.json", "r") as file:
        data = load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = Customer.create_customers(data["customers"])
    shops = Shop.create_shops(data["shops"])

    return fuel_price, customers, shops
