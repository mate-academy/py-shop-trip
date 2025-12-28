from __future__ import annotations

import math

from app.car.car import Car
from app.customer.customer import Customer
from app.shop.shop import Shop


class Config:
    def __init__(self, config_dict: dict) -> None:
        self.fuel_price = config_dict["FUEL_PRICE"]
        self.customers = self.__create_customers(config_dict["customers"])
        self.shops = self.__create_shops(config_dict["shops"])

    def get_cost_fuel(self, customer: Customer, shop: Shop) -> float:
        diff_x = (shop.location[0] - customer.location[0]) ** 2
        diff_y = (shop.location[1] - customer.location[1]) ** 2
        distance = math.sqrt(diff_x + diff_y)
        spend_fuel = customer.car.fuel_consumption * (distance * 2) / 100
        return round(spend_fuel * self.fuel_price, 2)

    @staticmethod
    def __create_customers(customers: list) -> list[Customer]:
        customer_objs = []
        for customer in customers:
            car = Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
            customer_objs.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    car
                )
            )

        return customer_objs

    @staticmethod
    def __create_shops(shops: list) -> list[Shop]:
        shop_objs = []
        for shop in shops:
            shop_objs.append(
                Shop(
                    shop["name"],
                    location=shop["location"],
                    products=shop["products"],
                )
            )

        return shop_objs
