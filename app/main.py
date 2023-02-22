import json
from copy import copy

from app.customers.creating_customers_classes import creating_customers_classes
from app.shops.creating_shops_classes import creating_shops_classes


def shop_trip():
    with open("config.json", "r") as file_in:
        data = json.load(file_in)

    fuel_price, customers, shops = data.values()
    classes_customers = creating_customers_classes(customers)
    classes_shop = creating_shops_classes(shops)

    for customer in classes_customers:
        print(f"{customer.name} has {customer.money} dollars")
        favorite_shop = None
        home_location = copy(customer.location)

        minimum_food_cost = 0

        for shop in classes_shop:

            cost_product = shop.costing_of_products(customer.product_cart)
            cost_road = customer.cost_of_road(shop.location, fuel_price)
            cost_all = cost_road * 2 + cost_product

            if not minimum_food_cost or minimum_food_cost > cost_all:
                minimum_food_cost = cost_all
                favorite_shop = shop

            print(f"{customer.name}'s trip to the {shop.name} costs {cost_all}")

        residue = round(customer.money - minimum_food_cost, 2)

        if residue < 0:
            print(f"{customer.name} doesn't have enough money to make purchase in any shop\n")
            continue

        print(f"{customer.name} rides to {favorite_shop.name}\n")
        customer.location = favorite_shop.location

        print(f"{favorite_shop.receipt(customer.product_cart, customer.name)}\n")

        print(f"{customer.name} rides home")
        customer.location = home_location

        print(f"{customer.name} now has {residue} dollars\n")


if __name__ == '__main__':
    shop_trip()
