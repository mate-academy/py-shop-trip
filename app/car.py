class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_price_distance(
            self, fuel_price: int | float,
            distance: int | float
    ) -> int | float:
        fuel_for_distance = distance * self.fuel_consumption / 100
        return fuel_for_distance * fuel_price
