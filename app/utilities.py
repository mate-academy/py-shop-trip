import json
import math


def parse_json(json_file: str) -> dict:
    with open(json_file) as file:
        return json.load(file)


def calculate_trip_cost(fuel_price: float,
                        fuel_consumption: float,
                        location_a: list,
                        location_b: list) -> float:

    distance = math.sqrt((location_b[0] - location_a[0]) ** 2
                         + (location_b[1] - location_a[1]) ** 2)

    print(fuel_price, distance, fuel_consumption)
    print(fuel_consumption * distance * fuel_price)
    return fuel_consumption * distance * fuel_price
