import json
import os
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        data = json.load(file)
    fuel_price, customers_, shops_ = data.values()

    customers = []
    for custom in customers_:
        car = Car(**custom["car"])
        customer = Customer(
            name=custom["name"],
            product_cart=custom["product_cart"],
            location=custom["location"],
            money=custom["money"],
            car=car
        )
        customers.append(customer)

    shops = []
    for some_shop in shops_:
        shop = Shop(
            name=some_shop["name"],
            location=some_shop["location"],
            products=some_shop["products"]
        )
        shops.append(shop)

    for customer in customers:
        customer_money = customer.money
        print(f"{customer.name} has {customer_money} dollars")
        trip_cost_dict = {}
        for shop in shops:
            total = 0
            dist_for_shop = customer.distance(shop.location)
            fuel_for_shop = customer.car.calculate_fuel_cost(
                dist_for_shop,
                fuel_price
            )
            products_cost = shop.products_cost(customer)
            total += round((products_cost + fuel_for_shop * 2), 2)
            trip_cost_dict[total] = shop
            print(f"{customer.name}'s trip to the {shop.name} costs {total}")
        if trip_cost_dict:
            if customer.money < min(trip_cost_dict):
                print(f"{customer.name} doesn't have enough"
                      f" money to make a purchase in any shop")
            else:
                total = min(trip_cost_dict)
                current_shop = trip_cost_dict[min(trip_cost_dict)]
                print(f"{customer.name} rides to {current_shop.name}\n")
                current_shop.print_check(customer)
                customer.ride_home(total)


shop_trip()
