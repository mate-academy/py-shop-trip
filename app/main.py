import os
import json
from typing import List
from app.customer.customer import Customer
from app.shop.shop import Shop


def creating(custom_class: List[dict], used_class) -> List[object]:
    class_list = []

    for class_ in custom_class:
        class_list.append(used_class(class_))
    return class_list


def create_shops(shops: List[dict]) -> List[object]:
    shops_list = creating(shops, Shop)

    return shops_list


def create_customers(customers: List[dict]) -> List[object]:
    customers_list = creating(customers, Customer)

    return customers_list


def shop_trip():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))) + "\\config.json"

    with open(__location__, "r") as json_file:
        data = json.load(json_file)

    FUEL_PRICE = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    customers = create_customers(customers)
    shops = create_shops(shops)

    for customer in customers:
        customer.trip(shops, FUEL_PRICE)


if __name__ == "__main__":
    shop_trip()
