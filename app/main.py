import json

from .customer.customer import Customer
from .shop.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    customers = [Customer(**customer)
                 for customer in data["customers"]]

    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        fuel_one_km_price = (customer.car.fuel_consumption / 100) * fuel_price
        customer.visit_shop(shops, fuel_one_km_price)
