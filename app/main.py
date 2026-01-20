import datetime
import json
import math
import os.path

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    customers = []
    shops = []
    with open(os.path.join("app", "config.json"), "r", encoding="utf-8") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    for customer in config["customers"]:
        customers.append(Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        ))

    for shop in config["shops"]:
        shops.append(Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        ))

    for customer in customers:
        trip_costs = []
        for shop in shops:
            dx = shop.location[0] - customer.location[0]
            dy = shop.location[1] - customer.location[1]
            distance = math.sqrt(dx ** 2 + dy ** 2) * 2

            fuel_needed = (customer.car.fuel_consumption / 100) * distance
            fuel_cost = fuel_needed * fuel_price

            total_products = 0
            for product in customer.product_cart:
                if shop.products.get(product, None) is None:
                    total_products = -1
                    break
                total_products += (shop.products[product]
                                   * customer.product_cart[product])
            if total_products == -1:
                continue
            trip_costs.append([total_products, fuel_cost, shop])

        print(f"{customer.name} has {customer.money} dollars")
        total_cost = trip_costs[0][0] + trip_costs[0][1]
        chosen_shop = trip_costs[0]
        for trip_shop_cost in trip_costs:
            if trip_shop_cost[0] + trip_shop_cost[1] < total_cost:
                total_cost = trip_shop_cost[0] + trip_shop_cost[1]
                chosen_shop = trip_shop_cost
            print(f"{customer.name}'s trip to the {trip_shop_cost[2].name} "
                  f"costs{(trip_shop_cost[0] + trip_shop_cost[1]): .2f}")

        if customer.money < total_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            if customers.index(customer) + 1 != len(customers):
                print()
            continue

        print(f"{customer.name} rides to {chosen_shop[2].name}")
        home_location = customer.location.copy()
        customer.location = chosen_shop[2].location.copy()
        print()
        date_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product in customer.product_cart:
            price = chosen_shop[2].products[product]
            amount = customer.product_cart[product]
            total = price * amount
            print(f"{customer.product_cart[product]} {product}s for"
                  f"{total: g} dollars")
        print(f"Total cost is {chosen_shop[0]}"
              f" dollars")
        print("See you again!")
        print()
        customer.location = home_location
        print(f"{customer.name} rides home")
        customer.money -= total_cost
        print(f"{customer.name} now has{customer.money: .2f} dollars")
        if customers.index(customer) + 1 != len(customers):
            print()
