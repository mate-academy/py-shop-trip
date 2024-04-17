class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self._brand = brand
        self._fuel_consumption = fuel_consumption

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    def calculate_fuel_costs(
        self,
        distance: float,
        fuel_price: float
    ) -> float:
        return distance * self._fuel_consumption / 100 * fuel_price

    def __repr__(self) -> str:
        return (
            f"Car: {{Brand: {self._brand}, "
            f"Fuel_consumption: {self._fuel_consumption}}}"
        )
