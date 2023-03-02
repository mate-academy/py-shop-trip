import math
from app.costumer import Customer
from app.shop import Shop


def trip_cost(fuel_price: float, costumer: Customer, shop: Shop) -> float:
    distance = math.dist(costumer.coords, shop.coords)
    total_fuel_cost = (costumer.fuel_cost(fuel_price) * distance) * 2

    total_price = 0
    for product in costumer.product_cart:
        total_price += costumer.product_cart[product] * shop.products[product]

    return round(total_fuel_cost + total_price, 2)
