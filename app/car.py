class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_of_way(
            self,
            fuel_price: int | float,
            distance: float
    ) -> int | float:
        return ((distance * self.fuel_consumption) / 100) * fuel_price
