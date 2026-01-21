import json
from app.customer import Customer, CONFIG_PATH
from app.shop import Shop
from math import sqrt


with open(CONFIG_PATH, "r") as file:
    config = json.load(file)
    fuel_price = config["FUEL_PRICE"]


def distance_cost(customer: Customer, shop: Shop) -> float:
    kilometers = sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )
    liters_needed = customer.car["fuel_consumption"] / 100
    return kilometers * liters_needed * fuel_price * 2
