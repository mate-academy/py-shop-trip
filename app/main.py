import json
from app.customers import Customers
from app.shops import Shops
from app.counting import counting


def shop_trip():
    with open("app/config.json", "r") as file:
        current_data = json.load(file)

    fuel_price = current_data["FUEL_PRICE"]
    customers = []
    shops = []

    for customer in current_data["customers"]:
        customers.append(
            Customers(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"],
            )
        )

    for shop in current_data["shops"]:
        shops.append(
            Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"],
            )
        )

    for customer in customers:
        counting(customer, shops, fuel_price)
