from app.car import Car
from app.customer import Customer
from app.shop import Shop
from app.home import Home


def init_all_class(info_dict):
    for customer in info_dict["customers"]:
        Car(customer["car"]["brand"],
            customer["car"]["fuel_consumption"])
        Home(customer["name"], customer["location"])
        Customer(customer["name"],
                 customer["product_cart"],
                 Home.homes[customer["name"]],
                 customer["money"],
                 Car.cars[customer["car"]["brand"]])
    for shop in info_dict["shops"]:
        Shop(shop["name"],
             shop["location"],
             shop["products"])
