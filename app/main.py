import json

from app.customer import Customer
from app.shop import Shops


def shop_trip() -> None:
    with open("config.json", "r") as info:
        information = json.load(info)

        fuel_price = information["FUEL_PRICE"]

        shops = [
            Shops(**shop)
            for shop in information["shops"]
        ]

        customers = [
            Customer(**client)
            for client in information["customers"]
        ]

        for customer in customers:
            customer.customers_wallet()
            Customer.customer_shop_trip(customer, shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
