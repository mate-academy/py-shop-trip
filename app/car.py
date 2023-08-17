import dataclasses


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float

    def __repr__(self) -> None:
        return self.brand
