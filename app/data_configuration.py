import json
import os

from app.car import Car
from app.shop import Shop
from app.customer import Customer


class Data:
    def __init__(self) -> None:
        self.customers = []
        self.shops = []
        self.fuel_price = None
        self.__file = None
        self.configuration()

    def configuration(self) -> None:
        self.find_path_to_config()
        big_dict = self.get_data_from_json()
        self.fuel_price = big_dict["FUEL_PRICE"]
        self.create_customers_obj(big_dict)
        self.create_shops_obj(big_dict)

    def find_path_to_config(self) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.__file = os.path.join(current_directory, "config.json")

    def get_data_from_json(self) -> dict:
        with open(self.__file, "r") as config_file:
            return json.load(config_file)

    def create_customers_obj(self, big_dict: dict) -> None:
        self.customers = [Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            )
        ) for customer in big_dict["customers"]]

    def create_shops_obj(self, big_dict: dict) -> None:
        self.shops = [Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        ) for shop in big_dict["shops"]]
