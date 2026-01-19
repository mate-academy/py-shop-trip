import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def product_price(
        shop_to_go: Shop,
        customer: Customer,
        product: str) -> float | int:
    shop_product = shop_to_go.products_provides[product]
    customer_product = customer.products_to_buy[product]
    product_cost = (shop_product * customer_product)
    return product_cost


def initialize_json() -> tuple:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    customer_list = []
    shop_list = []
    for customer in config["customers"]:
        customer_list.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            ),
        ))

    for shop in config["shops"]:
        shop_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        ))
    return fuel_price, customer_list, shop_list
