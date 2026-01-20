class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def get_way_value(self, location_from: list, location_to: list) -> float:
        way = ((location_to[0] - location_from[0]) ** 2 +
               + (location_to[1] - location_from[1]) ** 2) ** 0.5
        return way * self.fuel_consumption / 100

    def get_way_cost(self, fuel_cost: float,
                     location_from: list, location_to: list) -> float:
        return self.get_way_value(location_from, location_to) * fuel_cost
