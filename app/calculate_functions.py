import math
from typing import List, Dict


def calculate_distance(location1: List[int], location2: List[int]) -> float:
    return math.sqrt(
        (location1[0] - location2[0]) ** 2 + (location1[1] - location2[1]) ** 2
    )


def calculate_fuel_cost(
        distance: float, fuel_consumption: float, fuel_price: float
) -> float:
    return (distance / 100) * 2 * fuel_consumption * fuel_price


def calculate_total_cost(cart: Dict, products: Dict) -> float:
    return sum(
        item_value * products[item] for item, item_value in cart.items()
    )


def calculate_product_cost(cart: Dict, products: Dict) -> List:
    return [
        [item, item_value, item_value * products[item]]
        for item, item_value in cart.items()
    ]
