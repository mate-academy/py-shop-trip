import json

from app.instances.customer import Customer
from app.instances.shop import Shop


def file_handler(input_file: str) -> tuple:
    with open(input_file, "r") as file:
        config_data = json.load(file)
        fuel_cost = config_data["FUEL_PRICE"]
    return config_data, fuel_cost


def calculate_trip_distance(customer: Customer, shop: Shop) -> float:
    customer_x, customer_y = customer.location
    shop_x, shop_y = shop.location
    return ((shop_x - customer_x)**2 + (shop_y - customer_y)**2)**0.5


def fuel_cost_one_way(
    customer: Customer,
    fuel_price: float,
    shop: Shop
) -> float:
    return (fuel_price
            * calculate_trip_distance(customer, shop)
            * customer.car.fuel_consumption / 100)


def _products_cost(customer: Customer, shop: Shop) -> float:
    return round(
        sum(shop.products[product] * quantity
            for product, quantity in customer.product_cart.items()), 2
    )


def trip_cost(customer: Customer, fuel_price: float, shop: Shop) -> float:
    return round(fuel_cost_one_way(customer, fuel_price, shop) * 2
                 + _products_cost(customer, shop), 2)
