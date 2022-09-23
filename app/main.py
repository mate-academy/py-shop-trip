import json
import datetime

from app.home import Home
from app.customer import Customer
from app.shop import Shop
from app.init import init_all_class


def shop_trip():
    with open("app/config.json", "r") as info:
        info_dict = json.load(info)

    init_all_class(info_dict)

    for customer in Customer.customers.values():
        trip_to_shop = [[], []]

        print(f"{customer.name} has {customer.money} dollars")

        for number, shop in Shop.shops.items():
            x_loc = (customer.location[0] - shop.location[0]) ** 2
            y_loc = (customer.location[1] - shop.location[1]) ** 2
            road_to_shop = (x_loc + y_loc) ** 0.5
            fuel_one_km = customer.car.fuel_consumption / 100
            road = road_to_shop * info_dict["FUEL_PRICE"] * fuel_one_km
            milk = customer.product_cart["milk"] * shop.products["milk"]
            bread = customer.product_cart["bread"] * shop.products["bread"]
            butter = customer.product_cart["butter"] * shop.products["butter"]
            trip_to_shop[0].append(round(road * 2 + milk + bread + butter, 2))
            trip_to_shop[1].append(round(road * 2, 2))
            trip_to_shop.append([milk, bread, butter])

            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {trip_to_shop[0][number]}")

        trip_to_shop.append(["milk", "bread", "butter"])
        cheapest_trip = min(trip_to_shop[0])
        index_min = trip_to_shop[0].index(cheapest_trip)
        purchase_sum = sum(trip_to_shop[index_min + 2])
        cheapest_shop = Shop.shops[index_min]

        if cheapest_trip > customer.money:
            print(f"{customer.name} doesn't have enough money to"
                  f" make purchase in any shop")
            break

        print(f"{customer.name} rides to {cheapest_shop.name}\n")

        customer.location = cheapest_shop.location

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")

        for i in range(3):
            print(f"{customer.product_cart[trip_to_shop[-1][i]]} "
                  f"{trip_to_shop[-1][i]}s for "
                  f"{trip_to_shop[index_min + 2][i]} dollars")

        print(f"Total cost is {purchase_sum} dollars\n"
              f"See you again!\n")

        spent_money = trip_to_shop[1][index_min] + purchase_sum
        customer.money -= spent_money

        print(f"{customer.name} rides home")

        customer.location = Home.homes[customer.name]

        print(f"{customer.name} now has {customer.money} dollars\n")
