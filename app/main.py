import datetime
from math import inf

from app.customer import customer_initial
from app.shop import shop_initial
from app.utils import (
    calculate_trip_cost,
    calculate_distance,
    calculate_purchase_price
)


def shop_trip() -> None:
    customers = customer_initial()
    shops = shop_initial()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = inf
        preferred_shop_name = ""
        for shop in shops:
            distance = calculate_distance(
                customer.location,
                shop.location
            )
            trip_cost = calculate_trip_cost(
                distance,
                customer.car["fuel_consumption"]
            )
            totally_cost = calculate_purchase_price(trip_cost, customer, shop)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {totally_cost}")
            if totally_cost <= min_cost:
                preferred_shop_name = shop
                min_cost = totally_cost
        if min_cost > customer.money:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            return
        customer.location = preferred_shop_name.location
        print(f"{customer.name} rides to {preferred_shop_name.name}\n\n"
              f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
              f"\nThanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        total_buy = 0
        for buy_key, value in customer.products.items():
            for sell_key, cost in preferred_shop_name.product_cost.items():
                if buy_key == sell_key:
                    total_buy += value * cost
                    print(f"{value} {buy_key}s for {value * cost} dollars")
        print(f"Total cost is {total_buy} dollars\n"
              f"See you again!\n\n"
              f"{customer.name} rides home\n"
              f"{customer.name} now has"
              f" {round(customer.money - min_cost, 2)} dollars\n")
