import dataclasses
import json
import os


@dataclasses.dataclass
class Customers:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict


def convert_file():
    directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(directory, "config.json")
    with open(path, "r") as file:
        file_content = json.load(file)
    return file_content


def create_customer_list():
    persons = []
    for person in convert_file()["customers"]:
        customer = Customers(
            name=person["name"],
            product_cart=person["product_cart"],
            location=person["location"],
            money=person["money"],
            car=person["car"]
        )
        persons.append(customer)
    return persons
