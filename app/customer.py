import json
from typing import Union, List
from shop import Shop


class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def __init__(self, name, product_cart, location, money, car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __get__(self, instance, owner) -> list:
        pass

    @classmethod
    def load_info_customer(cls, read_data: dict) -> "Customer":
        return cls(
            name=read_data["name"],
            product_cart=read_data["product_cart"],
            location=read_data["location"],
            money=read_data["money"],
            car=read_data["car"]
        )


def read_from_json(data_file: str, what_information: str) -> Union[List[Union[Customer, Shop]], float]:

    with open(data_file, "r") as work_file:
        work_data = json.load(work_file)
        if what_information in work_data:
            test = []
            if isinstance(work_data[what_information], float):
                return work_data[what_information]
            for data in work_data[what_information]:
                test.append(data)
            return test


test_list = read_from_json("config.json", "customers")
custom_list = []
for test_ in test_list:
    custom_list.append(Customer.load_info_customer(test_))

# ttt = read_from_json("config.json", "customers")
# mmm = read_from_json("config.json", "shops")
# rrr = read_from_json("config.json", "FUEL_PRICE")
# ddd = read_from_json("config.json", "FUEL_PRIC")
yyy = 0
