from __future__ import annotations
import datetime
from customer import Customer
from shop import Shop


def print_receipt(
    customer: Customer,
    shop: Shop,
    products_cost: float
) -> None:
    now = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    print()
    print(f"Date: {now}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")

    for product, qty in customer.product_cart.items():
        if qty <= 0:
            continue
        if product not in shop.products:
            continue
        line_cost = qty * shop.products[product]
        print(f"{qty} {product}s for {line_cost} dollars")

    print(f"Total cost is {products_cost} dollars")
    print("See you again!")
    print()
