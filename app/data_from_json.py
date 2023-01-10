import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop

with open("app/config.json", "r") as file:
    information = json.load(file)

fuel_price = information["FUEL_PRICE"]

customers = information["customers"]
list_of_customers = []
for customer in customers:
    list_of_customers.append(Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"])))

shops = information["shops"]
list_of_shops = []
for shop in shops:
    list_of_shops.append(Shop(
        shop["name"],
        shop["location"],
        shop["products"]))
