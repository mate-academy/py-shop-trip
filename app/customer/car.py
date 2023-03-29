class Car:
    """A class to create a customer`s car."""
    def __init__(self, parameters: dict) -> None:
        self.brand = parameters["brand"]
        self.fuel_consumption = parameters["fuel_consumption"]
