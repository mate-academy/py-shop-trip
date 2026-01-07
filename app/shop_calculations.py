from datetime import datetime

from app.trip_calculations import calculate_distance, calculate_gas_price
from app.customer import Customer
from app.shop import Shop


def estimate_total_cost(
        gas_price: float,
        customer: Customer,
        shop: Shop) -> float:

    total_price = 0
    distance = calculate_distance(customer.location, shop.location)
    gas_price = calculate_gas_price(
        gas_price,
        customer.car["fuel_consumption"],
        distance)
    total_price += gas_price * 2
    for product, amount in customer.product_cart.items():
        price = shop.products[product]
        total_price += amount * price
    return total_price


def shopping(customer: Customer, shop: Shop) -> None:
    dt = datetime(2021, 1, 4, 12, 33, 41)

    formatted_dt = dt.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {formatted_dt}")

    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    total_price = 0
    for product, amount in customer.product_cart.items():
        price = shop.products[product]
        cost = amount * price
        total_price += cost

        if isinstance(cost, float):
            if cost.is_integer():
                display_cost = int(cost)
            else:
                display_cost = cost
        if isinstance(cost, int):
            display_cost = cost

        print(f"{amount} {product}s for {display_cost} dollars")
    print(f"Total cost is {total_price} dollars")
    print("See you again!")
