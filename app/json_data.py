import json
import math

from app.shop import Shop
from app.customer import Customer


def create_elements() -> tuple:
    with open("app/config.json") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = Customer.create_customers(data["customers"])
    shops = Shop.create_shops(data["shops"])
    return fuel_price, customers, shops


def distance(point1: list[int], point2: list[int]) -> float:
    return math.sqrt(
        (point2[0] - point1[0]) ** 2
        + (point2[1] - point1[1]) ** 2
    )


def shopping(customer: Customer, shop: Shop) -> int:
    total = 0
    shop.receipt = "You have bought: \n"
    for product in customer.product_cart:
        product_price = customer.product_cart[product] * shop.products[product]
        total += product_price
        shop.receipt += (
            f"{customer.product_cart[product]} {product}s "
            f"for {product_price} dollars\n"
        )
    shop.receipt += f"Total cost is {total} dollars"
    return total
