from __future__ import annotations

from app.customers import Customers
from app.shops import Shops


def shop_trip() -> None:

    customers_ls = Customers.create_customers_list()
    shops_ls = Shops.create_shops_list()

    for customer in customers_ls:
        print(f"{customer.name} has {customer.money} dollars")

        min_price = 10_000
        cheapest_shop = shops_ls[0]
        for shop in shops_ls:
            trip_cost = customer.count_road_price(shop)
            products_cost = customer.count_grocery_price(shop)
            full_price = trip_cost + products_cost
            if min_price > full_price:
                min_price = full_price
                cheapest_shop = shop

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {full_price}")

        if min_price > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            return
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        customer.location = cheapest_shop.location
        customer.money -= min_price

        cheapest_shop.shopping(customer)
