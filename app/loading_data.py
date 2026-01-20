import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def loading_data() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    Car.fuel_price = fuel_price

    for customer in config["customers"]:
        car = Car(**customer.pop("car"))
        Customer(car=car, **customer)

    for shop in config["shops"]:
        Shop(**shop)
