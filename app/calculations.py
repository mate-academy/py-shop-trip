import json
from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def calculate_trip_price(
        customer: Customer,
        shop: Shop,
        fuel_price: float
) -> float:
    distance = (
        (shop.location[0] - customer.location[0]) ** 2
        + (shop.location[1] - customer.location[1]) ** 2
    ) ** 0.5

    litres_used = distance * customer.car.fuel_consumption / 100

    trip_price = litres_used * fuel_price
    return trip_price * 2


def calculate_total_price(customer: Customer, shop: Shop) -> float:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]

    total_price = 0

    total_price += calculate_trip_price(customer, shop, fuel_price)
    for product_cart, quantity in customer.products_cart.items():
        if product_cart in shop.product_prices:
            price = quantity * shop.product_prices[product_cart]
            if customer.have_enough_money_to_perform_purchase(price):
                total_price += price

    return total_price


def purchases_info(customer: Customer, shop: Shop) -> None:
    print(f"{customer.name} rides to {shop.name}\n")
    current_time = datetime(
        2021, 1, 4, 12, 33, 41
    ).strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_time}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")

    purchases_price = 0
    for product_cart, quantity in customer.products_cart.items():
        if product_cart in shop.product_prices:
            price = shop.product_prices[product_cart] * quantity
            purchases_price += price
            price = (
                int(price)
                if float(price).is_integer()
                else round(price, 2)
            )
            print(
                f"{quantity} {product_cart}s for "
                f"{price}"
                f" dollars"
            )

    print(f"Total cost is {round(purchases_price, 2)} dollars")
    print("See you again!\n")
    print(f"{customer.name} rides home")
