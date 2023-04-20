from app.customer.customer import Customer, ProductCart
from app.shop.shop import Shop, PriceList
from app.trip.get_data import get_data

import math


def distance(customer: Customer, shop: Shop) -> float:
    """Calculate distance between customer and shop."""
    x1, y1 = customer.location
    x2, y2 = shop.location
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def fuel_price() -> float:
    """Return fuel_price"""
    return get_data()["FUEL_PRICE"]


def fuel_costs(customer: Customer, shop: Shop) -> float:
    """Calculate fuel costs"""
    fuel_consumption = customer.car.fuel_consumption
    distance_to_point = distance(customer, shop)
    return round(
        (fuel_consumption * distance_to_point * fuel_price() / 100) * 2, 2
    )


def shopping_cost(product_cart: ProductCart, price_list: PriceList) -> float:
    """Calculate cost of all purchases in one shop"""
    return (product_cart.milk * price_list.milk
            + product_cart.butter * price_list.butter
            + product_cart.bread * price_list.bread)
