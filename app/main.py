import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"


def shop_trip() -> None:
    with open(CONFIG_PATH) as f:
        data = json.load(f)
        Car.fuel_price = data["FUEL_PRICE"]
        list_of_customers = []
        list_of_shops = []
        for customer in data["customers"]:
            name = customer["name"]
            products = customer["product_cart"]
            location = customer["location"]
            money = customer["money"]
            car = Car(
                customer["car"]["brand"], customer["car"]["fuel_consumption"]
            )
            list_of_customers.append(
                Customer(name, products, location, money, car)
            )
        for shop in data["shops"]:
            name = shop["name"]
            location = shop["location"]
            products = shop["products"]
            list_of_shops.append(Shop(name, location, products))

        for customer in list_of_customers:
            print(f"{customer.name} has {customer.money} dollars")
            for shop in list_of_shops:
                print(customer.calculate_trip(shop))

            if not customer.where_to_go:
                continue
            cheapest_shop, cheapest_price = min(
                customer.where_to_go, key=lambda x: x[1]
            )
            if customer.money >= cheapest_price:
                print(customer.car.ride_to(customer, cheapest_shop))
                print()
                cheapest_shop.customer_bill(customer)
                print()
                print(customer.car.ride_to(customer))
                print()
            else:
                print(f"{customer.name} doesn't have "
                      f"enough money to make a purchase in any shop")
