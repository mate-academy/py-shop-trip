class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_consumption(
            self,
            location1: list[int, int],
            location2: list[int, int]
    ) -> int | float:
        distance = ((location2[0] - location1[0]) ** 2
                    + (location2[1] - location1[1]) ** 2
                    ) ** (1 / 2)

        return distance * self.fuel_consumption / 100
