import json

from app.customer import Customer
from app.shop import Shop


def shop_trip(filename: str = "app/config.json") -> None:
    # read info
    with open(filename, "r") as file:
        data = json.load(file)

    # create instances
    fuel_price: float = data.get("FUEL_PRICE")
    customers: list[Customer] = [
        Customer.from_dict(customer)
        for customer in data.get("customers", [])
    ]
    shops: list[Shop] = [
        Shop.from_dict(shop)
        for shop in data.get("shops", [])
    ]

    for customer in customers:
        customer.full_trip(shops, fuel_price)
