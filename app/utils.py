import math
from app.car import Car


def distance(loc1: list, loc2: list) -> float:
    """Расстояние между двумя точками"""
    dist = math.hypot(loc1[0] - loc2[0], loc1[1] - loc2[1])
    return math.floor(dist * 100) / 100


def travel_cost(distance_km: float, car: Car, fuel_price: float) -> float:
    """Стоимость топлива на указанное расстояние"""
    return (distance_km * car.fuel_consumption / 100) * fuel_price
