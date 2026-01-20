class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


def cost_of_road(
        used_fuel_in_dollars: float,
        distance_to_shop: float
) -> float:
    one_way_fuel_cost = (used_fuel_in_dollars * distance_to_shop) / 100
    return one_way_fuel_cost
