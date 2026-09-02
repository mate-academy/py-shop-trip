import json
import math


def distance_between_locations(cus_loc: list, shop_loc: list) -> float:
    return math.hypot(shop_loc[0] - cus_loc[0], shop_loc[1] - cus_loc[1])


def price_for_trip(distance: float,
                   fuel_for_one_km: float,
                   fuel_price: float) -> float:
    return distance * fuel_for_one_km * fuel_price


def all_cart_price(product_cart: dict, shop_products: dict) -> float:
    total = 0
    for product, count in product_cart.items():
        total += count * shop_products[product]
    return total


def load_config(filename: str) -> dict:
    with open(filename) as file:
        config = json.load(file)
        return config
