def calculate_distance(loc1: list, loc2: list) -> float:
    return ((loc2[0] - loc1[0]) ** 2 + (loc2[1] - loc1[1]) ** 2) ** 0.5


def calculate_fuel_cost(
        distance: float,
        fuel_consumption: float,
        fuel_price: float
) -> float:
    fuel_needed = (distance / 100) * fuel_consumption
    return fuel_needed * fuel_price
