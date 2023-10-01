class Car:
    def __init__(self, info_dict: dict) -> None:
        self.name = info_dict["brand"]
        self.fuel_consumption = info_dict["fuel_consumption"]
