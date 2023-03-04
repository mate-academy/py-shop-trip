import math

from module.car import Car
from module.customer import Customer
from module.shop import Shop


def shop_trip() -> None:
    Customer.load_from_json_info_about_customer()
    Car.load_from_json_info_about_car()
    Shop.load_from_json_info_about_shop()
    for customer in Customer.customers:

        product_cart_keys = []
        for product_name in customer.product_cart.keys():
            if product_name not in product_cart_keys:
                product_cart_keys.append(product_name)
        print(f"{customer.name} has {customer.money} dollars")
        possible_expences = {}
        nearest_store = {}

        for shop in Shop.shops:

            sum_products = sum(
                [shop.products[product] * customer.product_cart[product]
                 for product in product_cart_keys]
            )

            x2, y2 = customer.location
            x1, y1 = shop.location
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            carr = Car.fuel_consumption_to_car(customer.car)
            distance_price = 2 * (carr * distance / 100)

            cost_products = round(sum_products, 2)
            cost_trip_to_store = round(cost_products + distance_price, 2)
            possible_expences[shop.name] = cost_trip_to_store
            nearest_store[shop.name] = cost_products
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost_trip_to_store}")
        values_cost = [value for value in possible_expences.values()]
        go_to_ = ""
        for key, value in possible_expences.items():
            if value == min(values_cost):
                go_to_ += key
        distance_re = 0
        for key, value in nearest_store.items():
            if key == go_to_:
                distance_re = value

        if customer.money >= min(values_cost):
            print(f"{customer.name} rides to {go_to_}")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            break
        print(""
              "Date: 04/01/2021 12:33:41"
              f"Thanks, {customer.name}, for your purchase!"
              "You have bought: ")

        Shop.buy_product(customer, go_to_, product_cart_keys)
        print(f"Total cost is {round(distance_re, 2)} dollars"
              "See you again!"
              ""
              f"{customer.name} rides home"
              f"{customer.name} now has "
              f"{customer.money - min(values_cost)} dollars"
              "")
