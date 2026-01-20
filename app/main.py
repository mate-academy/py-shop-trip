from app.car import Car
from app.customer import Customer
from app.shop import Shop

import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop_data) for shop_data in config["shops"]]
    customers = []

    for customer_data in config["customers"]:
        car_data = customer_data.pop("car")
        car = Car(**car_data)
        customer = Customer(**customer_data, car=car)
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_options = []

        for shop in shops:
            round_trip_fuel = customer.calculate_trip_cost(
                shop.location, fuel_price) * 2
            total_purchase_cost = (
                shop.calculate_product_cart_cost(customer.product_cart))
            total_trip_cost = round_trip_fuel + total_purchase_cost

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(total_trip_cost, 2)}")
            if total_trip_cost <= customer.money:
                trip_options.append((total_trip_cost, shop,
                                     round_trip_fuel, total_purchase_cost))

        if trip_options:
            trip_options.sort(key=lambda x: x[0])
            _, cheapest_shop, fuel_cost, purchase_cost = trip_options[0]

            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location

            # друк чека — лише друк, без розрахунків
            cheapest_shop.generate_receipt(customer)

            print(f"{customer.name} rides home")
            customer.money -= (fuel_cost + purchase_cost)
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
