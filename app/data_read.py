import json
from typing import List

from app.car import Car
from app.customer import Customer
from app.shop import Shop


class DataRead:
    def __init__(self, config_file_path: str) -> None:
        with open(config_file_path, "r") as json_file:
            self._data = json.load(json_file)

    def get_customers(self) -> List[Customer]:
        customers = []
        for customer_data in self._data["customers"]:
            car_data = customer_data["car"]
            car = Car(car_data["brand"], car_data["fuel_consumption"])
            customer = Customer(customer_data["name"])
            customer.product_cart = customer_data["product_cart"]
            customer.location = customer_data["location"]
            customer.money = customer_data["money"]
            customer.car = car
            customers.append(customer)

        return customers

    def get_fuel_price(self) -> float:
        return self._data["FUEL_PRICE"]

    def get_shops(self) -> List[Shop]:
        shops = []
        for shop_data in self._data["shops"]:
            shop = Shop(shop_data["name"], shop_data["location"])
            shop.products = shop_data["products"]
            shops.append(shop)

        return shops
