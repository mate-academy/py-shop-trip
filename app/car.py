class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = float(fuel_consumption)

    def fuel_cost_for_distance(
        self,
        distance_km: float,
        fuel_price: float,
    ) -> float:
        liters = (self.fuel_consumption / 100.0) * float(distance_km)
        return liters * float(fuel_price)

    def __repr__(self) -> str:
        return (
            f"Car(brand={self.brand!r}, "
            f"fuel_consumption={self.fuel_consumption})"
        )
