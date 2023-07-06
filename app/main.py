import json

from pathlib import Path

from app.car import Car
from app.customer import Customers
from app.shop import Shop


def shop_trip() -> None:
    path = Path("app/config.json")
    with open(path, "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    shops_data = config_data["shops"]
    customers_data = config_data["customers"]

    shops = []
    cars = []
    customers = []
    best_choice = {}

    for shop_data in shops_data:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    for customer_data in customers_data:
        car_data = customer_data["car"]
        car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )
        cars.append(car)

        customer = Customers(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customers.append(customer)

    for customer in customers:
        customer.customer_money()
        for shop in range(len(shops)):

            total_trip_cost = customer.car.trip_cost(
                shops[shop],
                customer,
                fuel_price
            )
            milk_cost = customer.product_coast(shops[shop])[0]
            bread_cost = customer.product_coast(shops[shop])[1]
            butter_cost = customer.product_coast(shops[shop])[2]
            total_cost = round(
                total_trip_cost
                + sum(customer.product_coast(shops[shop])),
                2
            )

            best_choice[total_cost] = [
                shop,
                milk_cost,
                bread_cost,
                butter_cost
            ]

            rest_money = customer.money - min(best_choice)
            best_choice[total_cost].append(rest_money)

            customer.customer_best_choice(shops[shop], total_cost)

        milks_coast = best_choice[min(best_choice)][1]
        breads_coast = best_choice[min(best_choice)][2]
        butters = best_choice[min(best_choice)][3]
        buy_coast = milks_coast + breads_coast + butters
        index_shop = best_choice[min(best_choice)][0]

        if best_choice[min(best_choice)][4] < 0:
            customer.not_enough_money()
        else:
            customer.customer_rides_to_shop(shops[index_shop])

            shops[index_shop].customer_check(
                customer,
                milks_coast,
                breads_coast,
                butters,
                buy_coast
            )

            customer.customer_rides_home(min(best_choice))
