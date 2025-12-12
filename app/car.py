class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_needed(self, km: float) -> float:
        return km * self.fuel_consumption / 100

    def fuel_cost(self, km: float, fuel_price: float) -> float:
        return self.fuel_needed(km) * fuel_price
