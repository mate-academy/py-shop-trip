# flake8: noqa: VNE231
import math
import datetime

from app.customer import load_customers_from_config
from app.shop import load_shops_from_config
from app.car import load_fuel_price_from_config


def shop_trip() -> None:
    customers = load_customers_from_config()
    shops = load_shops_from_config()
    fuel_price = load_fuel_price_from_config()

    for i, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        best_price = float("inf")
        best_shop = None
        best_trip_cost = 0

        for shop in shops:
            x1, y1 = customer.location
            x2, y2 = shop.location
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            fuel_needed = (distance * 2) / 100 * customer.car.fuel_consumption
            fuel_cost = fuel_price * fuel_needed

            products_cost = 0

            for product, quantity in customer.product_cart.items():

                if product in shop.products:
                    product_price = shop.products[product]
                    products_cost += quantity * product_price
                else:
                    products_cost = float("inf")
                    break

            trip_cost = products_cost + fuel_cost

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )

            if trip_cost < best_price:
                best_price = trip_cost
                best_shop = shop
                best_trip_cost = trip_cost

        if best_price > customer.money:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )

        else:
            print(f"{customer.name} rides to {best_shop.name}")
            print()
            print(
                f"Date: "
                f"""{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}"""
            )
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            total_cost = 0

            for product, quantity in customer.product_cart.items():
                if product in best_shop.products:
                    product_price = best_shop.products[product]
                    item_cost = quantity * product_price
                    total_cost += item_cost

                    if quantity == 1:
                        print(
                            f"{quantity} {product} for {item_cost:g} dollars"
                        )
                    else:
                        print(
                            f"{quantity} {product}s for {item_cost:g} dollars"
                        )

            print(f"Total cost is {total_cost:g} dollars")

            print("See you again!")
            print()
            print(f"{customer.name} rides home")

            remaining_money = customer.money - best_trip_cost
            print(f"{customer.name} now has {remaining_money:.2f} dollars")
        if i < len(customers) - 1:
            print()


shop_trip()
