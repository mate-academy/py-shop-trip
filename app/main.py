import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        if customer.select_shop(shops, fuel_price):
            customer.make_purchases()
            customer.go_home()
