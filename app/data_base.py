import json


class DataBase:
    def __init__(self) -> None:
        with open("app/config.json", "r") as config:
            self.__data = json.load(config)

    def get_shops(self) -> None:
        return self.__data["shops"]

    def get_customers(self) -> None:
        return self.__data["customers"]

    def get_fuel_price(self) -> None:
        return self.__data["FUEL_PRICE"]
