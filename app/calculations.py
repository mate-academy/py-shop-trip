from app.customer import Customer
from app.shop import Shop

import math


def calculate_distance(location1: list[int], location2: list[int]) -> float:
    distance = math.dist(location1, location2)
    return distance


def calculate_fuel_cost(
        distance: float, fuel_consumption: float, fuel_price: float
) -> float:
    fuel_cost = distance * fuel_consumption / 100 * fuel_price
    return fuel_cost


def calculate_products_cost(product_cart: dict, shop_products: dict) -> float:
    total_cost = 0
    for product, quantity in product_cart.items():
        if product in shop_products:
            total_cost += shop_products[product] * quantity
    return total_cost


def calculate_trip_cost(
        customer: Customer, shop: Shop, fuel_price: float
) -> float:
    distance = calculate_distance(customer.location, shop.location)
    fuel_cost = calculate_fuel_cost(
        distance, customer.car.fuel_consumption, fuel_price
    )
    products_cost = calculate_products_cost(
        customer.product_cart, shop.products
    )
    total_cost = fuel_cost * 2 + products_cost
    return total_cost
