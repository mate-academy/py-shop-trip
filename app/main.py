import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")

    with open(path, "r") as f:
        data = json.load(f)

    for customer in data["customers"]:
        Customer(customer)

    for shop in data["shops"]:
        Shop(shop)

    Car.fuel_price = data["FUEL_PRICE"]

    for customer in Customer.all_customers:
        cheap_shop, total_spent = customer.choice_cheap_shoping(
            Shop.list_of_all_shops
        )
        if cheap_shop is None:
            continue
        else:
            customer.location = customer.car.travel(
                customer.name,
                cheap_shop.location,
                cheap_shop.name
            )
            print()
            cheap_shop.receipt(customer.name, customer.product_cart)

            customer.location = customer.car.travel(
                customer.name,
                customer.home,
                "home"
            )

            customer.remaining_money(total_spent)
