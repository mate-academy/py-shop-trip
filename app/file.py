import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


class OpenFile:
    @staticmethod
    def open_file_config(file_path: str) -> dict:
        with open(f"{file_path}", "rb") as config:
            data_config = dict(json.load(config))
            return data_config

    @staticmethod
    def creation_instances(
        data_config: dict
    ) -> tuple:
        customer_instances = []
        shop_instances = {}
        Car.fuel_price = data_config["FUEL_PRICE"]
        for customer in data_config.get("customers"):
            car = Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
            customer_instance = Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                car
            )
            customer_instances.append(customer_instance)
        for shop in data_config.get("shops"):
            shop_instance = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            shop_instances[shop["name"]] = shop_instance
        return customer_instances, shop_instances
