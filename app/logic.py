import os
import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def prepare_for_shop_trip() -> tuple:
    with open(os.path.join("app", "config.json")) as data_file:
        json_str = data_file.read()

    data_dict = json.loads(json_str)

    customers_list = [
        Customer(customer, Car(data_dict["FUEL_PRICE"], customer["car"]))
        for customer in data_dict["customers"]
    ]

    shops_list = [
        Shop(shop)
        for shop in data_dict["shops"]
    ]

    return customers_list, shops_list


def go_shopping(customer: Customer, selected_shop: Shop) -> None:
    customer.drive_to(selected_shop)
    customer.buy_products()
    customer.return_home()
    customer.check_wallet()


def plan_shop_trip(customer: Customer, shops: list) -> Shop | None:
    print(f"{customer.name} has {customer.money} dollars")

    if selected_shop := customer.choose_shop_out_of(shops):
        return selected_shop

    print(
        f"{customer.name} doesn't have enough money "
        "to make a purchase in any shop"
    )
