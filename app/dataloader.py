import json
import os
from app.cars import Car
from app.customers import Customer
from app.shops import Shop


class Dataloader:
    def __init__(self, name: str) -> None:
        self.name = name
        self.data = None
        self.load_file()
        self.create_shops()
        self.get_fuel_price()
        self.create_customers_and_cars()
        self.get_fuel_price()

    def load_file(self) -> None:
        with open(os.path.join("app", "config.json"), "r") as file:
            self.data = json.load(file)

    def get_fuel_price(self) -> None:
        Car.fuel_price = self.data["FUEL_PRICE"]

    def create_customers_and_cars(self) -> None:
        for customer in self.data["customers"]:
            Customer(customer["name"],
                     customer["product_cart"],
                     customer["location"],
                     customer["money"],
                     Car(customer["car"]["brand"],
                         customer["car"]["fuel_consumption"]))

    def create_shops(self) -> None:
        for shop in self.data["shops"]:
            Shop(shop["name"],
                 shop["location"],
                 shop["products"])
