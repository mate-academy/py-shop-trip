import json

from app.customer import Customer
from app.receipt import print_receipt
from app.shop import Shop


def shop_trip():
    with open("app/config.json") as input_file:
        info = json.load(input_file)

    fuel_price = info["FUEL_PRICE"]
    customers = []
    shops = []

    for customer in info["customers"]:
        customers.append(
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
        )
    for shop in info["shops"]:
        shops.append(
            Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
        )
    for customer in customers:
        print_receipt(customer, shops, fuel_price)
