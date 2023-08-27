import math
from typing import List, Dict


def calculate_distance(location1: List[int], location2: List[int]) -> float:
    return math.sqrt(
        (location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2
    )


def calculate_fuel_cost(
        distance: float, fuel_consumption: float, fuel_price: float
) -> float:
    return distance * fuel_consumption * fuel_price / 50


def calculate_total_cost(cart: Dict, products: Dict) -> float:
    return sum(cart[item] * products[item] for item in cart)


def calculate_product_cost(cart: Dict, products: Dict) -> List:
    return [[item, cart[item], cart[item] * products[item]] for item in cart]
