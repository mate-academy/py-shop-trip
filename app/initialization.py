import json

from customers.customer import Customer
from customers.car import Car
from app.shop import Shop


def customer_init(data: json) -> list:
    customers = []

    for customer in data.get("customers"):
        car = customer["car"]
        car_name = Car(car["brand"], car["fuel_consumption"])
        person = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car_name
        )
        customers.append(person)
    return customers


def shop_init(data: json) -> list:
    shops = []

    for shop in data.get("shops"):
        shop = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shops.append(shop)
    return shops
