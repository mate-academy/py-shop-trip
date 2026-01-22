import math


def trip_distance(
        coordinates1: list[int],
        coordinates2: list[int]
) -> int | float:
    one_way_distance = math.dist(coordinates1, coordinates2)
    return one_way_distance * 2


def fuel_costs(
        customer_location: list[int],
        shop_location: list[int],
        fuel_consumption: float,
        fuel_price: float
) -> int | float:
    distance = trip_distance(customer_location, shop_location)
    fuel_used = distance * fuel_consumption / 100
    return fuel_used * fuel_price
