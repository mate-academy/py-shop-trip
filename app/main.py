import datetime
import math
import json

from app.car import Car
from app.customer import Customers
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    shops_data = config_data["shops"]
    customers_data = config_data["customers"]
    dt = datetime.datetime(2021, 1, 4, 12, 33, 41)
    buy_date = dt.strftime("%d/%m/%Y %H:%M:%S")

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
        print(f"{customer.name} has {customer.money} dollars")
        for shop in range(len(shops)):

            distance = math.sqrt(
                (shops[shop].location[0] - customer.location[0]) ** 2
                + (shops[shop].location[1] - customer.location[1]) ** 2
            )
            total_trip_cost = round(
                (((distance / 100)
                  * customer.car.fuel_consumption
                  * fuel_price) * 2), 2
            )
            milk_cost = (
                customer.product_cart["milk"]
                * shops[shop].products["milk"]
            )
            bread_cost = (
                customer.product_cart["bread"]
                * shops[shop].products["bread"]
            )
            butter_cost = (
                customer.product_cart["butter"]
                * shops[shop].products["butter"]
            )
            total_cost = round(
                (total_trip_cost + milk_cost + bread_cost + butter_cost), 2
            )
            best_choice[total_cost] = [
                shop,
                milk_cost,
                bread_cost,
                butter_cost
            ]
            rest_money = customer.money - min(best_choice)
            best_choice[total_cost].append(rest_money)

            print(f"{customer.name}'s trip to the"
                  f" {shops[shop].name} costs {total_cost}")

        milks_coast = best_choice[min(best_choice)][1]
        breads_coast = best_choice[min(best_choice)][2]
        butters = best_choice[min(best_choice)][3]
        buy_coast = milks_coast + breads_coast + butters
        index_shop = best_choice[min(best_choice)][0]

        if best_choice[min(best_choice)][4] < 0:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {shops[index_shop].name}\n")
            print(f"Date: {buy_date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            print(f"{customer.product_cart['milk']}"
                  f" milks for {milks_coast} dollars")
            print(f"{customer.product_cart['bread']}"
                  f" breads for {breads_coast} dollars")
            print(f"{customer.product_cart['butter']}"
                  f" butters for {butters} dollars")
            print(f"Total cost is {buy_coast} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {customer.money - min(best_choice)}\n")


if __name__ == "__main__":
    shop_trip()
