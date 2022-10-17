import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car

with open("app/config.json", "r") as file_data:
    data = json.load(file_data)

fuel_price = data["FUEL_PRICE"]

customers_ls = []
cars_ls = []
shops_ls = []

for elem in data["customers"]:
    customers_ls.append(
        Customer(
            name=elem["name"],
            products_to_buy=elem["product_cart"],
            location=elem["location"],
            money=elem["money"],
            car=elem["car"]
        )
    )

    cars_ls.append(
        Car(
            brand=elem["car"]["brand"],
            fuel_consumption=elem["car"]["fuel_consumption"]
        )
    )

for elem in data["shops"]:
    shops_ls.append(
        Shop(
            name=elem["name"],
            location=elem["location"],
            products_price=elem["products"],
        )
    )
