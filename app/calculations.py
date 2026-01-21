import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def calculate_trip_cost(customer: Customer,
                        shop: Shop,
                        fuel_cost: float,
                        car: Car) -> float:
    total = 0
    for item in customer.products_to_buy:
        total += shop.available_products[item] * customer.products_to_buy[item]
    total += 2 * calculate_car_trip_price(
        customer.location,
        shop.location,
        fuel_cost,
        car.fuel_consumption)
    return round(total, 2)


def calculate_car_trip_price(
        point1: list[float],
        point2: list[float],
        fuel_cost: float,
        fuel_consumption: float
) -> float:
    distance = math.sqrt((point2[0] - point1[0])**2
                         + (point2[1] - point1[1])**2)
    return distance * (fuel_cost * fuel_consumption / 100)
