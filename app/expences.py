import math
import datetime

from app.customers import Customer
from app.shops import Shop


def find_min_cost(
        customer: Customer, shops: list[Shop], fuel_price: float
) -> tuple | None:
    budget = customer.money
    print(f"{customer.name} has {budget} dollars")
    (shop_head_to,
     total_cost,
     purchase_cost_min,
     _distance
     ) = [shops[0], 0, 0, 0]
    for shop in shops:
        purchase_cost = sum(
            [shop.products[product] * customer.product_cart[product]
             for product in customer.product_cart]
        )
        distance = math.sqrt(
            (customer.location[0] - shop.location[0]) ** 2
            + (customer.location[1] - shop.location[1]) ** 2
        )
        fuel_spend_cost = round(
            customer.car["fuel_consumption"] / 100
            * distance * 2 * fuel_price, 2)
        print(
            f"{customer.name}'s trip to the {shop.name} costs"
            f" {purchase_cost + fuel_spend_cost}")
        if purchase_cost + fuel_spend_cost == total_cost:
            if distance < _distance:
                shop_head_to, total_cost, purchase_cost_min, _distance = [
                    shop, purchase_cost + fuel_spend_cost, purchase_cost,
                    distance]
        elif (purchase_cost + fuel_spend_cost < total_cost
              or total_cost == 0):
            (shop_head_to,
             total_cost,
             purchase_cost_min,
             _distance) = [
                shop,
                purchase_cost + fuel_spend_cost,
                purchase_cost,
                distance
            ]
    if budget >= total_cost:
        print(f"{customer.name} rides to {shop_head_to.name}")
        return (shop_head_to, total_cost, purchase_cost_min)
    print(
        f"{customer.name} "
        f"doesn't have enough money to make a purchase in any shop")
    return None


def print_receipt(customer: Customer, expences_info: tuple) -> None:
    shop, total_cost, purchase_cost = expences_info
    purchase_info = ""
    for product in customer.product_cart:
        product_quantity = customer.product_cart[product]
        shop_product_quantity_cost = (product_quantity
                                      * shop.products[product])
        purchase_info += (
            f"{product_quantity} "
            f"""{product if product_quantity == 1
            else product + 's'} for """
            f"""{int(shop_product_quantity_cost)
            if int(shop_product_quantity_cost) == shop_product_quantity_cost
            else shop_product_quantity_cost} dollars\n"""
        )
    print(f"""
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
