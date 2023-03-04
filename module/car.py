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
    def load_from_json_info_about_car(cls) -> None:
        with open("../config.json", "r") as cars_file:
            customer_data = json.load(cars_file)
            for customer in customer_data["customers"]:
                car = cls(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
                cls.cars.append(car)

    @staticmethod
    def fuel_consumption_to_car(car: str) -> float:
        with open("../config.json", "r") as file_data:
            info = json.load(file_data)
            fuel_price = info["FUEL_PRICE"]
        for car_brand in Car.cars:
            if car_brand.brand == car:
                return car_brand.fuel_consumption * fuel_price
