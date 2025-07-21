import datetime
import json
import math


from app.car import car_list
from app.customer import customer_list
from app.shop import shop_list


with open("app/config.json") as config:
    data = json.load(config)
    fuel_price = data["FUEL_PRICE"]


def shop_trip() -> None:

    for index, customer in enumerate(customer_list):
        print(f"{customer.name} has {customer.money} dollars")
        trips_cost = {}

        for shop in shop_list:
            distance = math.sqrt(
                ((shop.location[0] - customer.location[0]) ** 2)
                + ((shop.location[1] - customer.location[1]) ** 2)
            )
            fuel_consumption_per_1_km = car_list[index].fuel_consumption / 100
            gasoline_cost = (
                (distance * fuel_consumption_per_1_km)
                * 2 * fuel_price
            )
            products_cost = 0
            for product in customer.product_cart:
                products_cost += (customer.product_cart[product]
                                  * shop.products[product])
            total = gasoline_cost + products_cost
            trips_cost[shop] = total
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(total, 2)}")

        if min(trips_cost.values()) > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        cheapest_trip = min(trips_cost.values())
        for shop in trips_cost:
            if trips_cost[shop] == cheapest_trip:
                print(f"{customer.name} rides to {shop.name}\n")

                timestamp = datetime.datetime.now().strftime(
                    "%d/%m/%Y %H:%M:%S"
                )
                print(f"Date: {timestamp}")
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought:")

                check_amount = 0
                for product in customer.product_cart:
                    product_cost = (customer.product_cart[product]
                                    * shop.products[product])
                    check_amount += product_cost
                    if product_cost.is_integer():
                        print(f"{customer.product_cart[product]} {product}s "
                              f"for {int(product_cost)} dollars")
                    else:
                        print(f"{customer.product_cart[product]} {product}s "
                              f"for {product_cost} dollars")

                if check_amount.is_integer():
                    print(f"Total cost is {int(check_amount)} dollars")
                else:
                    print(f"Total cost is {check_amount} dollars")

                print("See you again!\n")
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has "
                      f"{round(customer.money - cheapest_trip, 2)} dollars\n")
