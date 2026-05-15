import json
from decimal import Decimal

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = {}
    shops = {}

    with open("app/config.json", "r") as file:
        config_data = json.load(file)

    fuel_price = Decimal(str(config_data["FUEL_PRICE"]))

    for customer in config_data["customers"]:
        customer_product_cart = {}
        for key in customer["product_cart"]:
            customer_product_cart[key] = (
                Decimal(str(customer["product_cart"][key]))
            )
        customers[customer["name"]] = (
            Customer(
                customer["name"],
                customer_product_cart,
                tuple(customer["location"]),
                Decimal(str(customer["money"])),
                Car(
                    customer["car"]["brand"],
                    Decimal(str(customer["car"]["fuel_consumption"]))
                )
            )
        )

    for shop in config_data["shops"]:
        shop_products = {}
        for key in shop["products"]:
            shop_products[key] = (
                Decimal(str(shop["products"][key]))
            )
        shops[shop["name"]] = (
            Shop(
                shop["name"],
                tuple(shop["location"]),
                shop_products,
            )
        )

    for customer in customers.values():
        customer.shopping(shops, fuel_price)
