import math
from app.classes.car import Car


def fuel_costs(
        fuel_price: float,
        car: Car,
        customer_location: list,
        shop_location: list,
) -> float:
    consumption = car.fuel_consumption
    distance_km = round(
        math.sqrt(
            (shop_location[0] - customer_location[0])**2
            + (shop_location[1] - customer_location[1])**2
        ), 3
    )
    trip_to_shop = (distance_km / 100) * consumption * fuel_price * 2
    return round(trip_to_shop, 2)
