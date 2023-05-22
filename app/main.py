import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)

    customers = Customer.create_customers(data)
    shops = Shop.create_shops(data)
    [customer.select_cheapest_shop(shops) for customer in customers]


if __name__ == "__main__":
    shop_trip()
