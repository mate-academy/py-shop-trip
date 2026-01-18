import math
from decimal import Decimal
from typing import List
from app.customer import Customer
from app.shop import Shop


def calculate_distance(loc1: list, loc2: list) -> float:
    return math.sqrt(Decimal(loc1[0] - loc2[0]) ** 2
                     + Decimal(loc1[1] - loc2[1]) ** 2)


def calculate_trip(customers: List[Customer],
                   shops: List[Shop],
                   fuel_price: float) -> None:
    for customer in customers:
        price_of_products = {
            shop.name: {
                item: Decimal(customer.product_cart.get(item, 0))
                * Decimal(shop.products.get(item, 0))
                for item in customer.product_cart
            }
            for shop in shops
        }

        total_price = {
            shop.name: sum(
                Decimal(customer.product_cart.get(item, 0))
                * Decimal(shop.products.get(item, 0))
                for item in customer.product_cart
            )
            for shop in shops
        }

        fuel_sum = {}
        for shop in shops:
            distance = calculate_distance(customer.location,
                                          shop.location)

            fuel_used = (Decimal(distance)
                         * Decimal(customer.car.fuel_consumption / 100))
            fuel_cost = (Decimal(fuel_used)
                         * Decimal(fuel_price))
            total_fuel = fuel_cost * 2
            fuel_sum[shop.name] = float(round(total_fuel, 2))

        total_trip_cost = {
            shop_name: Decimal(total_price[shop_name])
            + Decimal(fuel_sum[shop_name])
            for shop_name in total_price
        }

        customer.price_of_products = price_of_products
        customer.total_price = total_price
        customer.fuel_sum = fuel_sum
        customer.total_trip_cost = total_trip_cost
