class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __repr__(self) -> str:
        return (f"Car(brand={self.brand}, "
                f"fuel_consumption={self.fuel_consumption})")

    def calculate_fuel_costs(
            self, distance_to_shop_and_home: float,
            fuel_price: float
    ) -> float:
        return (distance_to_shop_and_home * (self.fuel_consumption / 100)
                * fuel_price)
