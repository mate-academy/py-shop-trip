from app.service import (fuel_data,
                         customer_data,
                         shop_data,
                         distance)
from datetime import datetime


def shop_trip() -> None:
    fuel = fuel_data()
    customers = customer_data()
    shops = shop_data()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_ = None
        total_cost = 0
        cost_of_products = 0
        for shop in shops:
            cur_distance = round(distance(customer.location, shop.location), 2)
            trip_cost = round(customer.car.fuel_consumption
                              / 100 * cur_distance * fuel, 2)
            cost_products = sum(shop.products[key] * value
                                for key, value in customer.products.items())
            if shop_ is None:
                shop_ = shop
                total_cost = cost_products + trip_cost
            if total_cost > cost_products + trip_cost:
                shop_ = shop
                total_cost = cost_products + trip_cost
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost + cost_products}")
        if customer.money < total_cost:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            break
        print(f"{customer.name} rides to {shop_.name}")
        print()
        date = datetime(2021, 4, 1, 12, 33, 41)
        print(f"Date: {date.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        for key, value in customer.products.items():
            cost_of_products += value * shop_.products[key]
            print(f"{value} {key}s for {value * shop_.products[key]} dollars")
        print(f"Total cost is {cost_of_products} dollars")
        print("See you again!")
        print()
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money - total_cost} dollars")
        print()
