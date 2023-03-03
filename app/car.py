import json


class Car:
    cars = []

    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def add_to_car(cls) -> None:
        with open("app/config.json", "r") as cars_file:
            customer_data = json.load(cars_file)
            for customer in customer_data["customers"]:
                for key, value in customer.items():
                    if key == "car":
                        car = cls(
                            brand=value["brand"],
                            fuel_consumption=value["fuel_consumption"]
                        )
                cls.cars.append(car)

    @staticmethod
    def fuel_consumption_to_car(car: str) -> float:
        with open("app/config.json", "r") as file_data:
            info = json.load(file_data)
            fuel_price = info["FUEL_PRICE"]
        for i in Car.cars:
            if i.brand == car:
                return i.fuel_consumption * fuel_price
