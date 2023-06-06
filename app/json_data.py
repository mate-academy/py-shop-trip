import json
import math

from app.shop import Shop
from app.customer import Customer


def create_elements() -> tuple:
    with open("config.json") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = Customer.set_customer_from_file(data["customers"])
    shops = Shop.set_shop_from_file(data["shops"])
    return fuel_price, customers, shops


def distance(point1: list, point2: list) -> float:
    return math.sqrt(
        (point2[0] - point1[0]) ** 2
        + (point2[1] - point1[1]) ** 2
    )


def shopping(customer: Customer, shop: Shop) -> tuple:
    ttl_product_price = 0
    receipt = "You have bought:\n"
    for product in customer.product_cart:
        product_price = customer.product_cart[product] * shop.products[product]
        ttl_product_price += product_price
        receipt += (
            f"{customer.product_cart[product]} {product}s "
            f"for {product_price} dollars\n"
        )
    receipt += f"Total cost is {ttl_product_price} dollars"
    return ttl_product_price, receipt
