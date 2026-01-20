from __future__ import annotations
import datetime

from app.customer import Customer
from app.shop import Shop


def go_to_shop(customer: Customer, cheapest_shop: Shop) -> None:
    print(f"{customer.name} rides to {cheapest_shop.name}\n")

    customer_home = customer.location
    customer.location = cheapest_shop.location

    print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Thanks, {customer.name}, for you purchase!")
    print("You have bought: ")

    shopping_costs = shopping_list(
        customer.product_cart,
        cheapest_shop.products
    )

    print(f"Total cost is {shopping_costs} dollars")
    print("See you again!\n")
    print(f"{customer.name} rides home")

    customer.location = customer_home


def shopping_list(product_cart: dict, products: dict) -> float:
    costs = 0

    for product in product_cart:
        if product in products:
            spent_per_product = (product_cart[product] * products[product])
            costs += spent_per_product
            print(
                f"{product_cart[product]} {product}s "
                f"for {spent_per_product} dollars"
            )

    return costs
