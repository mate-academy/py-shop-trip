from app.customer.customer import Customer, ProductCart
from app.shop.shop import Shop, PriceList
from app.trip.get_data import _FUEL_PRICE

import math


def distance(customer: Customer, shop: Shop) -> float:
    """Calculate distance between customer and shop."""
    x1, y1 = customer.location
    x2, y2 = shop.location
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def fuel_price() -> float:
    """Return fuel_price"""
    return _FUEL_PRICE


def fuel_costs(customer: Customer, shop: Shop) -> float:
    """Calculate fuel costs"""
    fuel_consumption = customer.car.fuel_consumption
    distance_to_point = distance(customer, shop)
    return round(
        (fuel_consumption * distance_to_point * fuel_price() / 100) * 2, 2
    )


def shopping_cost(product_cart: ProductCart, price_list: PriceList) -> float:
    """Calculate cost of all purchases in one shop"""
    total_cost = 0
    for product, quantity in product_cart.__dict__.items():
        if product == "milk":
            total_cost += quantity * price_list.milk
        elif product == "butter":
            total_cost += quantity * price_list.butter
        elif product == "bread":
            total_cost += quantity * price_list.bread
    return total_cost
