class Car:

    def __init__(self, car_dictionary: dict) -> None:
        self.brand = car_dictionary.get("brand")
        # volume of fuel consumption for 100 kilometers
        self.fuel_consumption = car_dictionary.get("fuel_consumption")

    def __repr__(self) -> str:
        return (
            f"brand: {self.brand}, "
            f"fuel consumption: {self.fuel_consumption}"
        )

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Brand should be a string")
        self._brand = new_name

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value: float | int) -> None:
        if not (isinstance(new_value, float)
                or isinstance(new_value, int)):
            raise TypeError("Fuel consumption must be numeric!")
        if new_value < 0:
            raise ValueError("Fuel consumption can not be less than 0")
        self._fuel_consumption = new_value
