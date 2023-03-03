import math

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> str:

    Customer.add_to_customers()
    Shop.add_to_shops()
    Car.add_to_car()

    for customer in Customer.customers:
        print(f"{customer.name} has {customer.money} dollars")
        possible_expences = {}
        nearest_store = {}
        for shop in Shop.shops:

            price_milk = shop.products["milk"]\
                * customer.product_cart["milk"]
            price_bread = shop.products["bread"]\
                * customer.product_cart["bread"]
            price_butter = shop.products["butter"]\
                * customer.product_cart["butter"]

            x2, y2 = customer.location
            x1, y1 = shop.location
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            carr = Car.fuel_consumption_to_car(customer.car)
            distance_price = 2 * (carr * distance / 100)

            cost_products = round(price_milk + price_bread + price_butter, 2)
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
                  f"enough money to make purchase in any shop")
            break
        print("")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        Shop.buy_product(customer, go_to_)
        print(f"Total cost is {round(distance_re, 2)} dollars")
        print("See you again!")
        print("")
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - min(values_cost)} dollars")
        print("")
