import math
from app.Classes.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, sell_product: dict) -> None:
        self.name = name
        self.location = location
        self.product = sell_product


def trip_cost(customer: Customer, shop: Shop) -> float:
    dx = shop.location[0] - customer.location[0]
    dy = shop.location[1] - customer.location[1]
    distance = ((math.sqrt(dx ** 2 + dy ** 2) / 100)
                * customer.car["fuel_consumption"] * 2.4) * 2
    cost = sum([(customer.product_cart[product] * shop.product[product])
                for product in customer.product_cart])
    return cost + distance


def customer_service(customer: Customer, shop: Shop) -> None:
    print("Date: 04/01/2021 12:33:41")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought: ")
    for product in customer.product_cart:
        product_cart = customer.product_cart
        if (product_cart[product] * shop.product[product]) % 1 == 0:
            print(f"{product_cart[product]} {product}s "
                  f"for {round(product_cart[product] * shop.product[product])}"
                  f" dollars")
        else:
            print(
                f"{product_cart[product]} {product}s "
                f"for {product_cart[product] * shop.product[product]}"
                f" dollars")
    total_pay = sum([(customer.product_cart[product] * shop.product[product])
                     for product in customer.product_cart])
    print(f"Total cost is {total_pay} dollars")
    print("See you again!")
    print("")
