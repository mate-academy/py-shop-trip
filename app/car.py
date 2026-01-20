class Car:
    fuel_price = 0

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __str__(self) -> str:
        return (
            f"[Brand: {self.brand}, "
            f"Fuel_consumption: {self.fuel_consumption}]"
        )
