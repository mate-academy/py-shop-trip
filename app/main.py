from app.trip_cost_calculation import trip_cost_calculation
from app.customer import Customer
from app.print_check import check_printer
from app.shop import Shop
from app.car import Car
import json


def shop_trip() -> None:
    with open("app/config.json") as config:
        config_dict = json.load(config)

    fuel_price, customers_config, shops_config = config_dict.values()

    customers_list = [
        Customer(customer["name"],
                 customer["product_cart"],
                 customer["location"],
                 customer["money"],
                 Car(customer["car"]["brand"],
                     customer["car"]["fuel_consumption"]))
        for customer in customers_config
    ]

    shops_list = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in shops_config
    ]

    for customer in customers_list:
        min_cost = float("inf")
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_list:

            cost = trip_cost_calculation(
                customer.location,
                shop.location,
                customer.car.fuel_consumption,
                customer.product_cart,
                shop.products,
                fuel_price
            )
            total_cost = cost[0]
            product_cost = cost[1]

            if total_cost < min_cost:
                min_cost = total_cost
                min_products_cost = product_cost
                temp_shop = shop

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

        if min_cost > customer.money:
            print(f"{customer.name} doesn't have enough money to "
                  f"make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {temp_shop.name}\n")
        check_printer(customer, temp_shop, min_products_cost)

        print(f"{customer.name} rides home")
        customer.buy(min_cost)
        print(f"{customer.name} now has {customer.money} dollars\n")
