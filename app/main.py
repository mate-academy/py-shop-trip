from __future__ import annotations

from app.customers import Customers
from app.shops import Shops


def shop_trip() -> None:

    customers_ls = Customers.create_customers_list()
    shops_ls = Shops.create_shops_list()

    for customer in customers_ls:
        print(f"{customer.name} has {customer.money} dollars")
        cost_dict = {}
        for shop in shops_ls:
            trip_cost = customer.count_road_price(shop)
            products_cost = customer.count_grocery_price(shop)
            cost_dict[shop] = [trip_cost, products_cost]
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {sum(cost_dict[shop])}")

        cheapest_shop = min(sum(value) for value in cost_dict.values())
        if cheapest_shop > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make purchase in any shop")
            return
        for key, value in cost_dict.items():
            if sum(value) == cheapest_shop:
                shop_to_go = key
        print(f"{customer.name} rides to {shop_to_go.name}\n")
        customer.location = shop_to_go.location
        customer.money -= sum(cost_dict[shop_to_go])

        shop_to_go.shopping(customer)
