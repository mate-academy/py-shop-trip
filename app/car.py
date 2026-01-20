import json

with open("app/config.json", "r") as f:
    data = json.load(f)
    fuel_price = data["FUEL_PRICE"]


class Car:

    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price

    def __repr__(self) -> str:
        return f"{self.brand}"
