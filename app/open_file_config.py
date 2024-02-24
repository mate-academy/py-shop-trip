import json
from typing import Tuple, List
from app.car import Car
from app.customer import Customer
from app.shop import Shop


class OpenFileConfig:

    @staticmethod
    def take_data_from_config(
        file_path: str
    ) -> Tuple[List[Customer], List[Shop]]:
        customer_instances = []
        shop_instances = []
        with open(f"{file_path}", "rb") as config:
            data_config = dict(json.load(config))
            Car.fuel_price = data_config["FUEL_PRICE"]

            for customer in data_config.get("customers"):
                car = Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
                customer_instance = Customer(
                    name=customer["name"],
                    product_cart=customer["product_cart"],
                    location=customer["location"],
                    money=customer["money"],
                    car=car
                )
                customer_instances.append(customer_instance)

            for shop in data_config.get("shops"):
                shop_instance = Shop(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"]
                )
                shop_instances.append(shop_instance)
        return customer_instances, shop_instances
