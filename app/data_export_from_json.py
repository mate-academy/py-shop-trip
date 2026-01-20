import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop

with open("app/config.json", "r") as f:
    data = json.load(f)
    shops_data_list = data["shops"]
    customers_data_list = data["customers"]
    fuel_price = data["FUEL_PRICE"]

shops_data_dictionary = {
    shop["name"]: Shop(
        name=shop["name"],
        location=shop["location"],
        products=shop["products"]
    )
    for shop in shops_data_list
}

customers_data_dictionary = {
    customer["name"]: Customer(
        name=customer["name"],
        location=customer["location"],
        product_cart=customer["product_cart"],
        money=customer["money"],
        car=Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
    )
    for customer in customers_data_list
}
