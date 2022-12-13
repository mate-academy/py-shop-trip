from math import sqrt
from app.customer import Customer
from app.shop import Shop


def car_cost(customer: Customer,
             shop: Shop,
             fuel_price: float) -> float:

    first_location = customer.location
    second_location = shop.location

    x1 = first_location[0]
    y1 = first_location[1]
    x2 = second_location[0]
    y2 = second_location[1]
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    fuel_consumption = customer.car["fuel_consumption"]

    return 2 * distance * fuel_consumption / 100 * fuel_price
