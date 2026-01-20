import json
import os
from app.customer import Customer
from app.shop import Shop
from app.utils import format_price


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    shops = [Shop(shop_data) for shop_data in config["shops"]]

    for customer_data in config["customers"]:
        customer = Customer(customer_data)
        print(f"{customer.name} has {format_price(customer.money)} dollars")

        affordable_trips: list[tuple[float, Shop]] = []

        for shop in shops:
            if shop.has_all_products(customer.cart):
                trip_cost = customer.calculate_trip_cost(shop, fuel_price)
                product_cost = shop.calculate_cart_total(customer.cart)
                total_cost = trip_cost + product_cost
                print(
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {format_price(total_cost)}"
                )
                affordable_trips.append((total_cost, shop))

        if not affordable_trips:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            continue

        affordable_trips.sort(key=lambda x: x[0])
        cheapest_cost, cheapest_shop = affordable_trips[0]

        if customer.can_afford(cheapest_shop, fuel_price):
            customer.go_to_shop(cheapest_shop)
            customer.buy_products(cheapest_shop, fuel_price)
            customer.back_to_home()
            print(
                f"{customer.name} now has "
                f"{format_price(customer.money)} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
