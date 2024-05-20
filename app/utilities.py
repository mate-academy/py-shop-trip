import json

from app.classes.customer import Customer
from app.classes.shop import Shop


def parse_json(json_file: str) -> dict:
    with open(json_file) as file:
        return json.load(file)


def get_shopping_cost(customer: Customer, shop: Shop) -> float:
    cost = 0
    for item in customer.product_cart:
        cost += customer.product_cart[item] * shop.products[item]
    return cost


def calculate_trip_cost(fuel_price: float,
                        customer: Customer,
                        shop: Shop) -> float:
    distance = ((customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2) ** 0.5

    ride_cost = (customer.car.fuel_consumption / 100) * distance * fuel_price
    shopping_cost = get_shopping_cost(customer, shop)

    return ride_cost * 2 + shopping_cost
