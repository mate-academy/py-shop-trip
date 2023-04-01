import json

from app.classes.customer import Customer
from app.classes.product import Products
from app.classes.car import Car


def get_all_customers() -> list:
    customers = []
    with open("app/config.json", "r") as file:
        date_from_file = json.load(file)
        for customer in date_from_file["customers"]:
            customers.append(
                Customer(
                    customer["name"],
                    Products(
                        customer["product_cart"]["milk"],
                        customer["product_cart"]["bread"],
                        customer["product_cart"]["butter"]
                    ),
                    customer["location"],
                    customer["money"],
                    Car(
                        customer["car"]["brand"],
                        customer["car"]["fuel_consumption"]
                    )
                )
            )
        return customers
