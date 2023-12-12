import json
import math
import datetime
import os

from app.customers import Customer
from app.shops import Shop


def shop_trip() -> None:
    with (open(os.path.join(os.getcwd(), "app", "config.json"), "r")
          as data_json):
        data = json.load(data_json)
    customer_instances = [Customer(customer) for customer in data["customers"]]
    shop_instances = [Shop(shop) for shop in data["shops"]]
    for customer in customer_instances:
        budget = customer.money
        print(f"{customer.name} has {budget} dollars")
        (shop_head_to,
         total_cost,
         purchase_cost_min,
         _distance
         ) = [shop_instances[0], 0, 0, 0]
        for shop in shop_instances:
            purchase_cost = sum(
                [shop.products[product] * customer.product_cart[product]
                 for product in customer.product_cart]
            )
            distance = math.sqrt(
                (customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2
            )
            fuel_spend_cost = round(
                customer.car["fuel_consumption"] / 100 * distance * 2 * data[
                    "FUEL_PRICE"], 2)
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
            purchase_info = ""
            for product in customer.product_cart:
                product_quantity = customer.product_cart[product]
                shop_product_cost = (product_quantity
                                     * shop_head_to.products[product])
                purchase_info += (
                    f"{product_quantity} "
                    f"""{product if product_quantity == 1
                        else product + 's'} for """
                    f"""{int(shop_product_cost)
                    if int(shop_product_cost) == shop_product_cost
                    else shop_product_cost} dollars\n"""
                )

            print(
                f"""
Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
Thanks, {customer.name}, for your purchase!
You have bought:
{purchase_info.rstrip()}
Total cost is {purchase_cost_min} dollars
See you again!

{customer.name} rides home
{customer.name} now has {budget - total_cost} dollars
"""
            )
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a purchase in any shop")
