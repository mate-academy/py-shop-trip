class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def from_dict(cls, dictionary: dict) -> Car:
        return cls(
            brand=dictionary["brand"],
            fuel_consumption=dictionary["fuel_consumption"]
        )

    def fuel_consumed(self, distance: float) -> float:
        return (distance * self.fuel_consumption) / 100
