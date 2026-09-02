class Car:
    def __init__(self, car_info: dict) -> float:
        self.brand = car_info["brand"]
        self._fuel_consumption = car_info["fuel_consumption"]

    def get_fuel_cost(
            self,
            fuel_price: float,
            distance: float
    ) -> float:
        return self._fuel_consumption / 100 * distance * fuel_price