import json
from typing import Dict

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:

    config = load_config()
    if not config:
        return

    fuel_price = config["FUEL_PRICE"]
    customers = [
        create_customer(customer_config)
        for customer_config in config.get("customers", [])
    ]
    shops = [
        create_shop(shop_config) for shop_config in config.get("shops", [])
    ]

    for customer in customers:
        chosen_shop = customer.choose_shop(shops, fuel_price)
        if chosen_shop:
            customer.make_purchase(chosen_shop)
            customer.ride_home()


def load_config() -> Dict:
    with open("app/config.json", "r") as file:
        return json.load(file)


def create_car(car_config: Dict) -> Car:
    return Car(
        brand=car_config["brand"],
        fuel_consumption=car_config["fuel_consumption"]
    )


def create_shop(shop_config: Dict) -> Shop:
    return Shop(
        name=shop_config["name"],
        location=shop_config["location"],
        products=shop_config["products"]
    )


def create_customer(customer_config: Dict) -> Customer:
    return Customer(
        name=customer_config["name"],
        product_cart=customer_config["product_cart"],
        location=customer_config["location"],
        money=customer_config["money"],
        car=create_car(customer_config["car"])
    )


if __name__ == "__main__":
    shop_trip()
