import json

from app.customer import Customers
from app.shop import Shops
from app.car import Car


def shop_trip():
    with open("config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = Customers.create_customer(data["customers"])
        shops = Shops.add_shop(data["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        print(customer.count_cost(customer, shops))





shop_trip()


