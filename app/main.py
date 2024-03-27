import json
import os

from app.person import Person
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as config:
        objects_dict = json.load(config)

    fuel_price = objects_dict.get("FUEL_PRICE")
    shops: list[Shop] = []
    customers: list[Person] = []

    for customer in objects_dict.get("customers"):
        dict_car = customer.get("car")
        customers.append(
            Person
            (
                customer.get("name"),
                customer.get("product_cart"),
                customer.get("location"),
                customer.get("money"),
                Car(dict_car.get("brand"), dict_car.get("fuel_consumption"))
            )
        )

    for shop in objects_dict.get("shops"):
        shops.append(
            Shop
            (
                shop.get("name"),
                shop.get("products"),
                shop.get("location"),
            )
        )

    for customer in customers:
        customer.market_trip(shops, fuel_price)
