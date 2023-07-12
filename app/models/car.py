class Car:

    OWNER = None

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def motion_to_point(
            self,
            point: list,
            fuel_price: float
    ) -> float:
        distance = ((point[0] - self.OWNER.location[0]) ** 2
                    + (point[1] - self.OWNER.location[1]) ** 2) ** 0.5

        patrol = (distance / 100 * self.fuel_consumption * fuel_price) * 2
        return patrol
