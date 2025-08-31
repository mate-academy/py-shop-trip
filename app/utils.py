from math import sqrt


def count_distance_between_locations(location1: list,
                                     location2: list) -> float:
    return sqrt((location1[0] - location2[0]) ** 2
                + (location1[1] - location2[1]) ** 2)


def shop_cart_cost(product_cart: dict, price_map: dict) -> float:
    total_cost = 0.0
    for product, qty in product_cart.items():
        total_cost += price_map.get(product) * qty
    return total_cost
