import json


class Car:
    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


with open("app/config.json") as config:
    data = json.load(config)
    car_list = [Car(
        brand=car["car"]["brand"],
        fuel_consumption=car["car"]["fuel_consumption"])
        for car in data["customers"]]
