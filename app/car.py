class Car:
    def __init__(
            self,
            car_info: dict
    ) -> None:
        self.brand = car_info["brand"]
        self.fuel_consumption = car_info["fuel_consumption"]
