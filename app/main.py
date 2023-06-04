import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    Car.fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]
    for customer in customers:
        customer.choose_shop(shops)


if __name__ == "__main__":
    shop_trip()
