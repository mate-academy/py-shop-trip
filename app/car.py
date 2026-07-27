import json


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        with open("app/config.json", "r") as data_file:
            config = json.load(data_file)
        self.fuel_price = config["FUEL_PRICE"]
