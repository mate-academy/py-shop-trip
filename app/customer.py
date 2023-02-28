from app.car import Car
from math import dist


def unpack_customers(data: list) -> list:
    list_customers = []
    for customer in data:
        list_customers.append(Customer(customer))
    return list_customers


class Customer:
    def __init__(self, customer):
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"])

    def distance(self, shop_location):
        return dist(self.location, shop_location)
