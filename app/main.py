import datetime
import json

from app.customer import Customer
from app.shop import Shop


def calculate_distance(
        location1: list,
        location2: list
) -> float:
    return ((location1[0] - location2[0])**2
            + (location1[1] - location2[1])**2)**0.5


def calculate_fuel_cost(
        distance: float,
        fuel_price: float,
        fuel_consumption: float
) -> float:
    return (distance / 100) * fuel_consumption * fuel_price


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]
    customers = [Customer(**customer) for customer in customers_data]
    shops = [Shop(**shop) for shop in shops_data]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        min_cost = float("inf")
        for shop in shops:
            distance_to_shop = calculate_distance(
                customer.location, shop.location)
            fuel_cost_to_shop = calculate_fuel_cost(
                distance_to_shop, fuel_price, customer.car.fuel_consumption)
            total_cost = fuel_cost_to_shop
            for product, quantity in customer.product_cart.items():
                product_price = shop.products.get(product, 0)
                total_cost += product_price * quantity
            fuel_cost_to_home = calculate_fuel_cost(
                distance_to_shop, fuel_price, customer.car.fuel_consumption)
            total_cost += fuel_cost_to_home
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {round(total_cost, 2)}")
            if total_cost < min_cost and total_cost <= customer.money:
                min_cost = total_cost
                cheapest_shop = shop
        if cheapest_shop:
            customer.money -= min_cost
            customer.location = cheapest_shop.location
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            date = datetime.datetime.now()
            purchase_time = date.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {purchase_time}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            total_price = 0
            for product, quantity in customer.product_cart.items():
                product_price = cheapest_shop.products.get(product, 0)
                total_product_cost = product_price * quantity
                total_price += total_product_cost
                # if total_product_cost.is_integer():
                if ".0" not in str(total_product_cost):
                    print(f"{quantity} {product}s"
                          f" for {round(total_product_cost, 1)} dollars")
                else:
                    print(f"{quantity} {product}s "
                          f"for {int(total_product_cost)} dollars")
            print(f"Total cost is {round(total_price, 2)} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
