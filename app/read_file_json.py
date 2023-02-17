from json import load

from app.create_instance import create_customers, create_shops


def read_json() -> tuple:
    with open("app/config.json", "r") as file:
        data = load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = create_customers(data["customers"])
    shops = create_shops(data["shops"])

    return fuel_price, customers, shops
