class Car:
    fuel_price = 0

    def __init__(self, brand: str, fuel_cons: float | int) -> None:
        self.brand = brand
        self.fuel_cons = fuel_cons
