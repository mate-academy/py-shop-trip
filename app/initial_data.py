import json
from app.classes.customer import Customer
from app.classes.shop import Shop
from app.classes.car import Car


with open("app/config.json", "r") as file:
    data = json.load(file)


fuel_price = data["FUEL_PRICE"]
customers_data = data["customers"]
shops_data = data["shops"]


shops = [
    Shop(
        shop["name"],
        shop["location"],
        shop["products"],
    )
    for shop in shops_data
]


customers = [
    Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"],
            fuel_price
        )
    )
    for customer in customers_data
]
