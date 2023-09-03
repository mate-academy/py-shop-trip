import json
from typing import Union


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.amount_of_milk = product_cart["milk"]
        self.amount_of_bread = product_cart["bread"]
        self.amount_of_butter = product_cart["butter"]
        self.location = location
        self.money = money
        self.car_brand = car["brand"]
        self.car_fuel_consumption = car["fuel_consumption"]

    @classmethod
    def from_json(cls, json_string: Union[str, bytes]) -> object:
        json_dict = json.loads(json_string)
        return cls(**json_dict)


def customer_list() -> list:
    customers_list = []
    with open(
            "C:/Users/Expert/PycharmProjects/py-shop-trip/config.json", "r"
    ) as json_file:
        customers_data = json.loads(json_file.read())
        for customer in customers_data["customers"]:
            customers_list.append(Customer(**customer))
    return customers_list
