import json
from math import sqrt
from pathlib import Path


from app.customers import Customers
from app.shops import create_shops_objects


def calculate_cost_for_customer_for_every_shop(customer: Customers) -> dict:
    shops_ = create_shops_objects()
    base_dir = Path(__file__).resolve().parent

    with open(base_dir / "config.json", "r") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        calculated_prices = {}
        for shop in shops_:
            x_sub = shop.location[0] - customer.location[0]
            y_sub = shop.location[1] - customer.location[1]
            distance = (sqrt(x_sub ** 2 + y_sub ** 2))
            consumption = customer.car["fuel_consumption"]
            fuel_cost = (consumption / 100 * distance * fuel_price)
            product_cost = 0
            for product, amount in customer.product_cart.items():
                cost = amount * shop.products[product]
                product_cost += cost
            final_sum = round((fuel_cost * 2 + product_cost), 2)
            calculated_prices[shop.name] = final_sum
    return calculated_prices
