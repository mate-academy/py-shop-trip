import json
import os
from datetime import datetime

from app.data.customers.customers import Customer
from app.data.shops.shops import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file_data:
        _data: dict = json.load(file_data)
    fuel_price = _data["FUEL_PRICE"]
    customers: list = [Customer(**cust) for cust in _data["customers"]]
    shops: list = [Shop(**cust) for cust in _data["shops"]]

    out_print = ""
    for customer in customers:
        out_print += f"{customer.name} has {customer.money} dollars\n"

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            fuel_cost = 2 * fuel_price * (
                    (customer.location.x - shop.location.x) ** 2 +
                    (customer.location.y - shop.location.y) ** 2
            ) ** 0.5

            total_product_cost = sum(
                product_cost for product_cost in shop.products.values()
            )

            total_trip_cost = fuel_cost + total_product_cost

            out_print += (f"{customer.name}'s trip to the "
                          f"{shop.name} costs "
                          f"{total_trip_cost:.2f}\n")

            if total_trip_cost < min_trip_cost and customer.money >= total_trip_cost:
                min_trip_cost = total_trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.location = cheapest_shop.location

            out_print += (f"{customer.name} rides to {cheapest_shop.name}\n\n"
                          f"Date: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}\n"
                          f"Thanks, {customer.name}, for your purchase!\n"
                          f"You have bought:\n")
            for product, quantity in cheapest_shop.products.items():
                product_cost = quantity * (total_product_cost / sum(cheapest_shop.products.values()))
                out_print += f"{quantity} {product}s for {product_cost:.2f} dollars\n"
            out_print += (f"Total cost is {total_product_cost} dollars\n"
                          f"See you again!\n\n")

            customer.money -= total_product_cost
            out_print += (f"{customer.name} rides home\n"
                          f"{customer.name} now has {customer.money:.2f} dollars\n\n")
        else:
            out_print += f"{customer.name} doesn't have enough money to make a purchase in any shop\n\n"
    return out_print


if __name__ == "__main__":
    out = '''Bob has 55 dollars
    Bob's trip to the Outskirts Shop costs 28.21
    Bob's trip to the Shop '24/7' costs 31.48
    Bob's trip to the Central Shop costs 39.28
    Bob rides to Outskirts Shop

    Date: 04/01/2021 12:33:41
    Thanks, Bob, for your purchase!
    You have bought:
    4 milks for 12 dollars
    2 breads for 2 dollars
    5 butters for 12.5 dollars
    Total cost is 26.5 dollars
    See you again!

    Bob rides home
    Bob now has 26.79 dollars

    Alex has 41 dollars
    Alex's trip to the Outskirts Shop costs 17.14
    Alex's trip to the Shop '24/7' costs 15.95
    Alex's trip to the Central Shop costs 17.98
    Alex rides to Shop '24/7'

    Date: 04/01/2021 12:33:41
    Thanks, Alex, for your purchase!
    You have bought:
    2 milks for 4 dollars
    2 breads for 3 dollars
    2 butters for 6.4 dollars
    Total cost is 13.4 dollars
    See you again!

    Alex rides home
    Alex now has 25.05 dollars

    Monica has 12 dollars
    Monica's trip to the Outskirts Shop costs 15.65
    Monica's trip to the Shop '24/7' costs 16.84
    Monica's trip to the Central Shop costs 22.58
    Monica doesn't have enough money to make a purchase in any shop
    '''
    print(shop_trip())
