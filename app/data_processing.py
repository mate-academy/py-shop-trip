from copy import copy
from typing import List

from app.customers import Customer
from app.shop import Shop


def data_processing(
        fuel_price: float,
        classes_customers: List[Customer],
        classes_shop: List[Shop]
) -> None:
    for customer in classes_customers:
        favorite_shop = None
        home_location = copy(customer.location)
        minimum_food_cost = 0

        print(f"{customer.name} has {customer.money} dollars")

        for shop in classes_shop:
            cost_product = shop.costing_of_products(customer.product_cart)
            cost_road = customer.cost_of_road(shop.location, fuel_price)
            cost_all = round(cost_road * 2 + cost_product, 2)

            if not minimum_food_cost or minimum_food_cost > cost_all:
                minimum_food_cost = cost_all
                favorite_shop = shop

            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost_all}"
            )

        residue = round(customer.money - minimum_food_cost, 2)

        if residue < 0:
            print(
                f"{customer.name} doesn't have enough"
                f" money to make purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {favorite_shop.name}\n")
        customer.location = favorite_shop.location

        print(
            f"{favorite_shop.receipt(customer.product_cart, customer.name)}\n"
        )

        print(f"{customer.name} rides home")
        customer.location = home_location

        print(f"{customer.name} now has {residue} dollars\n")
