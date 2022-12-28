class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float | int,
            fuel_price: float | int
    ) -> None:
        self._brand = brand
        self._fuel_consumption = fuel_consumption / 100
        self._fuel_price = fuel_price

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def fuel_consumption(self) -> float:
        return self._fuel_consumption

    def cost_per_km(self) -> float:
        return self._fuel_consumption * self._fuel_price
