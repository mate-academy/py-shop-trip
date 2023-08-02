class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, first_location: list, second_location: list, fuel_price: float) -> float:

        distance = ((first_location[0] - second_location[0]) ** 2 +
                    (first_location[1] - second_location[1]) ** 2) ** 0.5

        return (self.fuel_consumption / 100) * distance * fuel_price * 2
