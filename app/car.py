class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_cost_of_trip(
            self,
            current_location: list[int],
            destination: list[int],
            fuel_price: float
    ) -> float:
        distance = Car.calculate_distance(current_location, destination)
        needed_fuel = distance * (self.fuel_consumption / 100)
        return needed_fuel * fuel_price

    @staticmethod
    def calculate_distance(
            current_location: list[int],
            destination: list[int],
    ) -> float:
        return ((destination[0] - current_location[0]) ** 2
                + (destination[1] - current_location[1]) ** 2) ** 0.5
