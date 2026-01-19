import datetime

import math

from app.file_handler import product_price, initialize_json


def shop_trip() -> None:
    fuel_price, customer_list, shop_list = initialize_json()
    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        for shop in shop_list:
            product_cost = 0
            first_point = (shop.location[0] - customer.location[0])**2
            second_point = (shop.location[1] - customer.location[1])**2
            destination = math.sqrt(first_point + second_point)
            fuel_consumption = customer.car.fuel_consumption
            fuel_cost = (destination / 100 * fuel_consumption * fuel_price * 2)

            for product in customer.products_to_buy:
                product_cost += product_price(shop, customer, product)

            trip_cost = round(product_cost + fuel_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_cost: .2f}")
            trip_costs[trip_cost] = (shop, product_cost)

        cheapest_trip = min(trip_costs.keys())
        shop_to_go, product_cost = trip_costs[cheapest_trip]
        if customer.money >= cheapest_trip:
            print(f"{customer.name} rides to {shop_to_go.name}\n")
            customer.location = shop_to_go.location
            current_date = datetime.datetime.now()
            print("Date: " + str(current_date.strftime("%d/%m/%Y %H:%M:%S")))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product in customer.products_to_buy:
                shop_product = shop_to_go.products_provides[product]
                customer_product = customer.products_to_buy[product]
                print(f"{customer.products_to_buy[product]} {product}s for "
                      f"{(customer_product * shop_product): .2f} dollars")

            print(f"Total cost is {product_cost: .2f} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {(customer.money - cheapest_trip): .2f} dollars\n")

        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
