class Car:
    def __init__(self, config: dict) -> None:
        self.brand = config["brand"]
        self.fuel_consumption = config["fuel_consumption"]
