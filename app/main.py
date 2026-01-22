import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    def create_objects() -> None:
        with open("app/config.json", "r") as file:
            config = json.load(file)

        for element in config["customers"]:
            Customer(
                element["name"],
                element["product_cart"],
                element["location"],
                element["money"],
                element["car"],
            )
        Customer.fuel_price = config["FUEL_PRICE"]

        for element in config["shops"]:
            Shop(
                element["name"],
                element["location"],
                element["products"],
            )
    create_objects()

    Customer.console_info()
