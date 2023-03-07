import json

from app.car import Car
from app.customer import Customer
from app.shops import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        file_info = json.load(file)
    shops = [Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    ) for shop in file_info["shops"]]

    for customer in file_info["customers"]:
        new_customer = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"])
        )
        new_customer.money()
        new_customer.customer_in_shop(shops)
