import json


from app.shop import Shop
from app.customer import Customer
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def create_customers_list(config_data: dict) -> list:
    customers_list = []
    for customer in config_data["customers"]:
        name = customer["name"]
        product_cart = customer["product_cart"]
        location = customer["location"]
        money = customer["money"]
        car = customer["car"]
        customers_list.append(Customer(
            name,
            product_cart,
            location,
            money,
            car
        ))
    return customers_list


def create_shops_list(config_data: dict) -> list:
    shops_list = []
    for shop in config_data["shops"]:
        name = shop["name"]
        location = shop["location"]
        products = shop["products"]
        shops_list.append(Shop(name, location, products))
    return shops_list


def shop_trip():
    with open(BASE_DIR / "config.json", "r") as file:
        config_data = json.load(file)
    fuel_price = config_data["FUEL_PRICE"]
    customers_list = create_customers_list(config_data)
    shops_list = create_shops_list(config_data)
    for customer in customers_list:
        customer.visit_shop(shops_list, fuel_price)
