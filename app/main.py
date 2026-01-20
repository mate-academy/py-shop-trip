import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    customers = [Customer(customer["name"],
                          customer["product_cart"],
                          customer["location"],
                          customer["money"],
                          Car(customer["car"]["brand"],
                              customer["car"]["fuel_consumption"]))
                 for customer in data["customers"]]
    Car.fuel_price = data["FUEL_PRICE"]
    shops = [Shop(shop["name"],
                  shop["location"],
                  shop["products"])
             for shop in data["shops"]]
    for customer in customers:
        customer.go_to_shop(shops)
