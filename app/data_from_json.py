import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_info() -> dict:
    with open("app/config.json", "r") as file:
        information = json.load(file)
    return information


def get_fuel_price() -> float:
    fuel_price = get_info()["FUEL_PRICE"]
    return fuel_price


def get_customers() -> list:
    customers = get_info()["customers"]
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
    return list_of_customers


def get_shops() -> list:
    shops = get_info()["shops"]
    list_of_shops = []
    for shop in shops:
        list_of_shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]))
    return list_of_shops
