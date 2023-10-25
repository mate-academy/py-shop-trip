import json

from .customer.customer import Customer
from .car.car import Car
from .shop.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    customers = [Customer(name=customer["name"],
                          products=customer["product_cart"],
                          location=customer["location"],
                          money=customer["money"],
                          car=Car(**customer["car"]))
                 for customer in data["customers"]]

    shops = [Shop(name=shop["name"],
                  location=shop["location"],
                  products=shop["products"]) for shop in data["shops"]]

    for customer in customers:
        fuel_one_km_price = (customer.car.fuel_consumption / 100) * fuel_price
        customer.visit_shop(shops, fuel_one_km_price)
