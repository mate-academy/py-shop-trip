import json

from app.customer import Customer
from app.shop import Shop
from app.calculation import cost_calculation


def shop_trip():
    with open("app/config.json", "r") as file:
        current_data = json.load(file)

    fuel_price = current_data["FUEL_PRICE"]
    customers = []
    shops = []

    for customer in current_data["customers"]:
        customers.append(
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"],
            )
        )

    for shop in current_data["shops"]:
        shops.append(
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"],
            )
        )

    for customer in customers:
        cost_calculation(customer, shops, fuel_price)
