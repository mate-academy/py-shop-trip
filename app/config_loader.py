import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def load_data() -> tuple[float, list[Customer], list[Shop]]:
    config_path = Path(__file__).with_name("config.json")

    with config_path.open("r") as config:
        data = json.load(config)

    customers = [
        Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                brand=customer_data["car"]["brand"],
                fuel_consumption=customer_data["car"]["fuel_consumption"],
            ),
        )
        for customer_data in data["customers"]
    ]

    shops = [
        Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"],
        )
        for shop_data in data["shops"]
    ]

    return data["FUEL_PRICE"], customers, shops
