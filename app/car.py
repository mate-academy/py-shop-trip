class Car:
    def __init__(self, data: dict) -> None:
        self.brand = data["brand"]
        self.fuel_consumption = data["fuel_consumption"]

    def calc_fuel_cost(self, distance_km: float, fuel_price: float) -> float:
        liters = distance_km * (self.fuel_consumption / 100.0)
        return liters * fuel_price
