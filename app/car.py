class Car:
    __fuel_cost = 0.0

    def __init__(self,
                 brand: str,
                 fuel_consumption: float) -> None:
        self.brand = brand
        self.__fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self,
                            distance: float) -> float:
        return (self.__fuel_consumption * distance / 100) * self.__fuel_cost

    @classmethod
    def set_fuel_cost(cls, fuel_cost: float) -> None:
        cls.__fuel_cost = fuel_cost
