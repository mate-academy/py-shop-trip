import json
from app.customer import calculate_km_trip
import os


def calculate_money_trip() -> list:
    fuel = []
    first = []
    second = []
    third = []
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as f:
        place = json.load(f)

    km = calculate_km_trip()

    for car in place["customers"]:
        fuel.append(car["car"]["fuel_consumption"])

    for distance in km[:3]:
        result = (distance / 100) * fuel[0]
        first.append(result)

    for distance in km[3:6]:
        result = (distance / 100) * fuel[1]
        second.append(result)

    for distance in km[6:]:
        result = (distance / 100) * fuel[2]
        third.append(result)

    return [first, second, third]


def calculate_price() -> list:
    price = []
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "config.json")
    with open(path, "r") as f:
        fuel = json.load(f)
    fuel_used = calculate_money_trip()

    for distances in fuel_used:
        for distance in distances:
            result = round(distance * fuel["FUEL_PRICE"], 2)
            price.append(result)
    return price
