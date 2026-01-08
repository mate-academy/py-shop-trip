import datetime

from app.trip_calculations import calculate_distance, calculate_gas_price
from app.customer import Customer
from app.shop import Shop


def estimate_total_cost(
        gas_price: float,
        customer: Customer,
        shop: Shop) -> float:

    total_price = 0
    distance = calculate_distance(customer.location, shop.location)
    one_way_fuel_cost = calculate_gas_price(
        gas_price,
        customer.car["fuel_consumption"],
        distance)
    total_price += one_way_fuel_cost * 2
    for product, amount in customer.product_cart.items():
        price = shop.products[product]
        total_price += amount * price
    return total_price


def shopping(customer: Customer, shop: Shop) -> None:
    dt = datetime.datetime.now()

    print(f"Date: {dt}")

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
                display_cost = round(cost, 2)
        if isinstance(cost, int):
            display_cost = cost

        print(f"{amount} {product}s for {display_cost} dollars")
    print(f"Total cost is {total_price} dollars")
    print("See you again!")
