import json

from app.product import Product
from app.car import Car
from app.cart import Cart
from app.shop import Shop
from app.customer import Customer

with open("app/config.json", "r") as data_file:
    data_from_file = json.loads(data_file.read())

FUEL_PRICE = data_from_file.get("FUEL_PRICE")


def shop_trip() -> None:
    result = ""

    for customer in data_from_file.get("customers"):
        result += (
            Customer(
                customer.get("name"),
                [Cart(product, amount) for product, amount
                 in customer.get("product_cart").items()],
                customer.get("location"),
                customer.get("money"),
                Car(
                    customer.get("car").get("brand"),
                    customer.get("car").get("fuel_consumption"))
            ).print_report([(
                Shop(
                    shop.get("name"),
                    shop.get("location"),
                    ([Product(product, price) for product, price in
                      shop.get("products").items()])))
                for shop in data_from_file.get("shops")])
        )

    print(result[:-2])
