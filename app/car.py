from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float


@dataclass
class Location:
    x_: int
    y_: int

    def __repr__(self) -> str:
        return f"({self.x_}, {self.y_})"
