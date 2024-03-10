import json


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.location = customer["location"]
        self.product_cart = customer["product_cart"]
        self.money = customer["money"]
        self.car_brand = customer["car"]["brand"]
        self.car_fuel_consumption = customer["car"]["fuel_consumption"]


with open("app/config.json") as file:
    data = json.load(file)

try:
    customers = data["customers"]
    customers_list = [Customer(customer) for customer in customers]
except KeyError:
    raise Exception("Customers data is missing")
