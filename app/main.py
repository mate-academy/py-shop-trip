import json

from app.customer.car import Car
from app.customer.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config_dict = json.loads(config.read())

    Car.fuel_price = config_dict["FUEL_PRICE"]

    customers = [Customer(
        customer["name"],
        customer["location"],
        customer["product_cart"],
        customer["money"],
        Car(customer["car"]["brand"], customer["car"]["fuel_consumption"])
    ) for customer in config_dict["customers"]]

    shops = [Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    ) for shop in config_dict["shops"]]

    for customer in customers:
        customer.pick_shop(shops)
        if customer.chosen_shop.shop:
            customer.make_a_purchase()
            customer.ride_home()
