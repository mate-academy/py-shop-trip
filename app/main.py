from __future__ import annotations
from app.data import process_json_data
import datetime


def shop_trip() -> None:
    data = process_json_data()

    fuel_price = data[0]
    customers = data[1]
    shops = data[2]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = [None, float("inf")]
        for shop in shops:
            total_cost = customer.calculate_total_cost(fuel_price, shop)
            if total_cost < cheapest_shop[1]:
                cheapest_shop[0] = shop
                cheapest_shop[1] = total_cost
            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_cost}")

        if customer.money > cheapest_shop[1]:
            print(f"{customer.name} rides to {cheapest_shop[0].name}")
            print(
                "\nDate:",
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            )
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            total_products_cost = 0
            for key, value in customer.product_cart.items():
                cost_per_product = (
                    customer.product_cart[key] * cheapest_shop[0].products[key]
                )
                if (isinstance(cost_per_product, float)
                        and cost_per_product.is_integer()):
                    cost_per_product = int(cost_per_product)
                total_products_cost += cost_per_product
                print(f"{value} {key}s for {cost_per_product} dollars")

            print(f"Total cost is {total_products_cost} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - cheapest_shop[1]} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
