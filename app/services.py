import math

from app.customer import Customer
from app.shop import Shop


def calculate_range_to_shop(customer: Customer, shop: Shop) -> float:
    self_x, self_y = customer.location
    shop_x, shop_y = shop.location

    x_axis = self_x - shop_x
    y_axis = self_y - shop_y

    return math.sqrt((x_axis**2) + (y_axis**2))


def calculate_fuel_consume(
        customer: Customer,
        kilometers: float | int
) -> float | int:
    return kilometers * customer.car.fuel_consumption / 100


def calculate_fuel_price(
    fuel_consume: float | int, fuel_price: float | int
) -> float | int:
    return fuel_price * fuel_consume


def calculate_trip_price(
    customer: Customer, shop: Shop, fuel_price: float | int
) -> float | int:
    to_shop_range = calculate_range_to_shop(customer, shop)
    fuel_consume = calculate_fuel_consume(customer, to_shop_range)

    return calculate_fuel_price(fuel_consume, fuel_price)
