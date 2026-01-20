import json

from app.customer import Customer, Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_data = json.load(file)
    Car.change_fuel_price(json_data["FUEL_PRICE"])
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in json_data["shops"]
    ]

    for customer_list in json_data["customers"]:
        customer = Customer(
            customer_list["name"],
            customer_list["product_cart"],
            customer_list["location"],
            customer_list["money"],
            customer_list["car"]
        )
        customer.do_shopping(shops)
