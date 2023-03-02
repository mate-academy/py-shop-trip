from __future__ import annotations
import math
from typing import Any

from app.customer import Customer
from app.shop import Shop


def count_trip_to_shop_value(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> Any:   # Shop | float doesn't work, have no idea how to make it other way
    result = {}
    for shop in shops:
        km_to_the_shop = math.sqrt(
            (customer.location[0] - shop.location[0]) ** 2
            + (customer.location[1] - shop.location[1]) ** 2)

        trip_to_shop_value = \
            (customer.car.fuel_consumption * km_to_the_shop) / 100 * fuel_price

        purchase_costs = sum(
            shop.products[product] * customer.product_cart[product]
            for product in shop.products
        )

        total_costs = round(purchase_costs + trip_to_shop_value * 2, 2)

        result[shop.name] = total_costs

        print(f"{customer.name}'s trip to the {shop.name} costs {total_costs}")

    cheapest_shop = min(result, key=result.get)
    min_costs = min(result.values())

    for shop in shops:
        if shop.name == cheapest_shop:
            return shop, min_costs
