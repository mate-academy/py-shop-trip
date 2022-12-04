import json
from app.colculater import Calculater

from app.shops import Shops
from app.customers import Customers


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)

    fuel_price = info["FUEL_PRICE"]
    customers = []
    shops = []

    for customer in info["customers"]:
        customers.append(
            Customers(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"],
            )
        )
    for shop in info["shops"]:
        shops.append(
            Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"],
            )
        )
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        Calculater(customer, shops, fuel_price).calculate()
