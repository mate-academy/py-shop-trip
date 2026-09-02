import json
import math


def distance_between_locations(customer_location: list,
                               shop_location: list) -> float:
    return math.hypot(shop_location[0] - customer_location[0],
                      shop_location[1] - customer_location[1])


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
