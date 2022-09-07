import json
from app.customer import Customer
from app.shop import Shop
from app.receipt import print_receipt


def shop_trip():
    with open("app/config.json") as config:
        current_info = json.load(config)

    fuel_price = current_info["FUEL_PRICE"]
    customers = []
    shops = []

    for customer in current_info["customers"]:
        customers.append(
            Customer(
                name=customer['name'],
                product_cart=customer['product_cart'],
                location=customer['location'],
                money=customer['money'],
                car=customer['car']
            )
        )
    for shop in current_info["shops"]:
        shops.append(
            Shop(
                name=shop['name'],
                location=shop['location'],
                products=shop['products'],
            )
        )

    for customer in customers:
        print_receipt(customer, shops, fuel_price)
