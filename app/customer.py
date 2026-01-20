import json
import math
import os


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


def calculate_km_trip() -> list:
    distance = []
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as f:
        trip = json.load(f)
    for person in trip["customers"]:
        for shop in trip["shops"]:
            location_person = person["location"]
            location_shop = shop["location"]
            x1, y1 = location_person
            x2, y2 = location_shop
            transform = (math.hypot((x2 - x1), (y2 - y1)) * 2)
            distance.append(transform)
    return distance
