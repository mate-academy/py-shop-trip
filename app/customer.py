import json


with open("config.json", "r") as f:
    data = json.load(f)
data_customers = data["customers"]


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: int, car: dict):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


customers = []
for human in data_customers:
    customers.append(Customer(human["name"],
                              human["product_cart"],
                              human["location"],
                              human["money"],
                              human["car"]))
