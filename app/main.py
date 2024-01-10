import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(**shop_data) for shop_data in data["shops"]]

    customers = [Customer(**customer_data,
                          car=Car(**customer_data["car"]))
                 for customer_data in data["customers"]]

    for customer in customers:
        customer.make_purchase(shops, fuel_price)
