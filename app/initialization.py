import json

from customers.customer import Customer
from app.shop import Shop


def customer_init(data: json) -> list:
    return [Customer(**customer) for customer in data["customers"]]


def shop_init(data: json) -> list:
    return [Shop(**shop) for shop in data.get("shops")]
