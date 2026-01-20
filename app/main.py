import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        customers = data["customers"]
        shops = data["shops"]
        customers_instance = []
        for customer in customers:
            car_instance = Car(brand=customer["car"]["brand"],
                               fuel_consumption=customer["car"]
                               ["fuel_consumption"])
            customer_instance = Customer(name=customer["name"],
                                         product_cart=customer["product_cart"],
                                         location=customer["location"],
                                         money=customer["money"],
                                         car=car_instance)
            customers_instance.append(customer_instance)
        shops_instance = []
        for shop in shops:
            shop_instance = Shop(name=shop["name"],
                                 location=shop["location"],
                                 products=shop["products"])
            shops_instance.append(shop_instance)

        for customer in customers_instance:
            customer.print_info(shops_instance, fuel_price)
