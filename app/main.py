import os
import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:

    absolute_path = os.path.dirname(__file__)
    relative_path = "config.json"
    full_path = os.path.join(absolute_path, relative_path)

    with open(full_path) as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]

    customers = []
    shops = []

    for customer_data in customers_data:
        name = customer_data["name"]
        product_cart = customer_data["product_cart"]
        location = customer_data["location"]
        money = customer_data["money"]
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])

        customer = Customer(name, location, money, product_cart, car)
        customers.append(customer)

    for shop_data in shops_data:
        name = shop_data["name"]
        location = shop_data["location"]
        products = shop_data["products"]

        shop = Shop(name, location, products)
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}

        for shop in shops:
            distance = customer.find_distance(shop.shop_location)
            fuel_cost = customer.car.calculate_price(distance, fuel_price)
            product_cost = shop.calculate_product_cost(customer.product_cart)

            total_cost = fuel_cost * 2 + product_cost
            trip_costs[shop] = total_cost

            print(f"{customer.name}'s trip to the "
                  f"{shop.shop_name} costs {round(total_cost, 2)}")

        min_cost_shop = min(trip_costs, key=trip_costs.get)

        if customer.money >= min(trip_costs.values()):
            print(f"{customer.name} rides to {min_cost_shop.shop_name}\n")

            customer.make_purchase(min_cost_shop)
            print(f"\n{customer.name} rides home")
            customer.money -= min(trip_costs.values())
            print(f"{customer.name} now "
                  f"has {round(customer.money, 2)} dollars\n")

        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


shop_trip()
