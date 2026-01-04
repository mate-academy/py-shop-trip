import datetime
import math

from app.modules.customer import Customer
from app.modules.shop import Shop


def calculate_distance_between_points(
    point1: list[int],
    point2: list[int],
) -> float:
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def calculate_trip_cost(
    customer: Customer,
    shop: Shop,
    fuel_price: float,
) -> float:
    distance_to_shop = calculate_distance_between_points(
        shop["location"],
        customer["location"],
    )

    fuel_cost = (
        distance_to_shop * customer["car"]["fuel_consumption"]
        / 100 * fuel_price * 2
    )

    product_cost = sum(
        shop["products"][product] * customer["product_cart"][product]
        for product in customer["product_cart"].keys()
    )
    return round(fuel_cost + product_cost, 2)


def shop_in_store(customer: Customer, shop: Shop) -> None:
    print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f'Thanks, {customer["name"]}, for your purchase!')
    print("You have bought:")
    total_cost = 0
    for product, quantity in customer["product_cart"].items():
        cost = quantity * shop["products"][product]
        total_cost += cost
        cost = int(cost) if cost % 1 == 0 else cost
        print(f"{quantity} {product}s for {(cost)} dollars")

    print(f"Total cost is {total_cost} dollars")
    print("See you again!\n")
