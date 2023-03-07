import json

from typing import List

from app.client_resources.Point2D import Point2d
from app.client_resources.customer import Customer, ServerWithFuelData
from app.shop_resources.shop import Shop
from app.client_resources.car import Car


def create_shops(shops: list[dict]) -> List[Shop]:
    return [Shop(shop_data["name"],
                 Point2d(shop_data["location"]),
                 shop_data["products"]) for shop_data in shops]


def process_customers_list() -> List[Customer]:
    try:
        with open("app/config.json", "r") as f:
            world_data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Loading problem, file/fpath"
                                f" {f} doesn't exist.")

    ServerWithFuelData.fuel_price = world_data["FUEL_PRICE"]

    return [Customer(name=customer["name"],
                     product_cart=customer["product_cart"],
                     location=Point2d(customer["location"]),
                     money=customer["money"],
                     car=Car(**customer["car"]),
                     known_shops=create_shops(world_data["shops"]))
            for customer in world_data["customers"]]


def shop_trip() -> None:
    customers = process_customers_list()
    for customer in customers:
        customer.wake_up_and_ride()
