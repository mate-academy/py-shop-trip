import math


class Car:
    """Car that calculates travel cost based on fuel consumption."""

    def __init__(
            self,
            brand: str,
            fuel_consumption: float,
            location: list[int]
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.home_location = location

    @classmethod
    def setup_car(
            cls,
            car_dict: dict,
            location: list[int]
    ) -> "Car":
        """Create Car instance from dictionary config."""
        return cls(car_dict["brand"], car_dict["fuel_consumption"], location)

    def __repr__(self) -> str:
        return (
            f"Brand: {self.brand}\n"
            f"Fuel consumption per 100 km: {self.fuel_consumption}"
        )

    @staticmethod
    def get_distance(
            current_location: list[int],
            shop_location: list[int]
    ) -> int | float:
        """Return distance between two points."""
        cx, cy = current_location
        sx, sy = shop_location
        return math.sqrt((cx - sx) ** 2 + (cy - sy) ** 2)
