import math
import datetime

from app.customers import Customer
from app.shops import Shop


def get_purchase_cost(customer: Customer, shop: Shop) -> float:
    return sum(
        (
            shop.products[product] * customer.product_cart[product]
            for product in customer.product_cart
        )
    )


def get_distance(customer: Customer, shop: Shop) -> float:
    return math.sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )


def find_min_cost(
    customer: Customer, shops: list[Shop], fuel_price: float
) -> tuple | None:
    budget = customer.money
    print(f"{customer.name} has {budget} dollars")
    (shop_head_to, total_cost, purchase_cost_min, distance) = [
        shops[0],
        0,
        0,
        0,
    ]
    for shop in shops:
        purchase_cost = get_purchase_cost(customer, shop)
        _distance = get_distance(customer, shop)
        fuel_spent_cost = round(
            customer.car["fuel_consumption"]
            / 100
            * _distance
            * 2
            * fuel_price,
            2,
        )
        _total_cost = purchase_cost + fuel_spent_cost
        print(f"{customer.name}'s trip to the {shop.name} costs {_total_cost}")
        if _total_cost == total_cost:
            if _distance < distance:
                shop_head_to, total_cost, purchase_cost_min, distance = [
                    shop,
                    _total_cost,
                    purchase_cost,
                    _distance,
                ]
        elif _total_cost < total_cost or total_cost == 0:
            (shop_head_to, total_cost, purchase_cost_min, distance) = [
                shop,
                _total_cost,
                purchase_cost,
                _distance,
            ]
    if budget >= total_cost:
        print(f"{customer.name} rides to {shop_head_to.name}")
        return (shop_head_to, total_cost, purchase_cost_min)
    print(
        f"{customer.name} "
        f"doesn't have enough money to make a purchase in any shop"
    )


def print_receipt(customer: Customer, expences_info: tuple) -> None:
    shop, total_cost, purchase_cost = expences_info
    purchase_info = ""
    for product in customer.product_cart:
        product_quantity = customer.product_cart[product]
        shop_product_quantity_cost = product_quantity * shop.products[product]
        if int(shop_product_quantity_cost) == shop_product_quantity_cost:
            shop_product_quantity_cost = int(shop_product_quantity_cost)
        purchase_info += (
            f"{product_quantity} "
            f"""{product if product_quantity == 1
            else product + 's'} for {shop_product_quantity_cost} dollars\n"""
        )
    print(
        f"""
Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
Thanks, {customer.name}, for your purchase!
You have bought:
{purchase_info.rstrip()}
Total cost is {purchase_cost} dollars
See you again!

{customer.name} rides home
{customer.name} now has {customer.money - total_cost} dollars
"""
    )
