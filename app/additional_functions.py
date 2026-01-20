import math


def calculate_distance(location1: list, location2: list) -> float:
    x1, y1 = location1
    x2, y2 = location2

    dx = x2 - x1
    dy = y2 - y1

    return math.sqrt(dx ** 2 + dy ** 2)


def calculate_product_cost(product_cart: dict, shop_products: dict) -> float:
    return sum(quantity * shop_products[product]
               for product, quantity in product_cart.items()
               if product in shop_products)
