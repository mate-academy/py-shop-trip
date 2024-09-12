class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int | float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_consumption(
            self,
            source: list[int],
            destination: list[int]
    ) -> int | float:
        distance = ((destination[0] - source[0]) ** 2
                    + (destination[1] - source[1]) ** 2
                    ) ** (1 / 2)

        return distance * self.fuel_consumption / 100
