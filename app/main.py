import json
import os
from math import dist

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")

    with open(config_path, "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    _customers = data["customers"]
    _shops = data["shops"]

    shops: list[Shop] = []
    for _shop in _shops:
        shop = Shop(
            name=_shop["name"],
            location=_shop["location"],
            products=_shop["products"]
        )
        shops.append(shop)

    for _customer in _customers:
        customer = Customer(
            name=_customer["name"],
            product_cart=_customer["product_cart"],
            location=_customer["location"],
            money=_customer["money"],
            car=Car(
                brand=_customer["car"]["brand"],
                fuel_consumption=_customer["car"]["fuel_consumption"]
            )
        )
        print(f"{customer.name} has {customer.money} dollars")
        available = []
        for shop in shops:
            cart_price = shop.calculate_cart_price(customer.product_cart)
            if cart_price is None:
                continue
            distance_km = dist(customer.location, shop.location)
            fuel_cost = (
                customer.car.calculate_fuel_cost(distance_km, fuel_price)
            )
            trip_cost = 2 * fuel_cost + cart_price
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(trip_cost, 2)}"
            )
            available.append((shop, trip_cost))

        if not available:
            print("No shop is suitable for shop trip")
            return

        costs = [cost[1] for cost in available]
        if customer.money >= min(costs):
            min_index = costs.index(min(costs))
            target_shop: Shop = shops[min_index]
            print(f"{customer.name} rides to {target_shop.name}\n")
            customer.change_location(target_shop.location)
            target_shop.print_receipt(customer)
            print(f"{customer.name} rides home")
            customer.change_location(customer.home)
            remaining_money = customer.money - min(costs)
            customer.money = remaining_money
            print(
                f"{customer.name} now has {round(customer.money, 2)} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
