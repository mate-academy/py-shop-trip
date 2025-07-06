import json
import os
from app.customer import Customer
from app.shop import Shop
from app.utils import format_price


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price: float = config["FUEL_PRICE"]
    shops = [Shop(shop_data) for shop_data in config["shops"]]

    for c_data in config["customers"]:
        customer = Customer(c_data)
        print(f"{customer.name} has {format_price(customer.money)} dollars")

        possible_trips: list[tuple[float, Shop]] = []

        for shop in shops:
            if shop.has_all_products(customer.cart):
                fuel_cost = customer.calculate_trip_cost(shop, fuel_price)
                product_cost = shop.get_cart_cost(customer.cart)
                total_cost = fuel_cost + product_cost
                cost_str = format_price(total_cost)
                print(
                    f"{customer.name}'s trip to the {shop.name} "
                    f"costs {cost_str}"
                )
                possible_trips.append((total_cost, shop))

        if not possible_trips:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            continue

        possible_trips.sort(key=lambda x: x[0])
        cheapest_cost, cheapest_shop = possible_trips[0]

        if customer.can_afford(cheapest_shop, fuel_price):
            customer.go_to_shop(cheapest_shop)
            customer.buy_products(cheapest_shop, fuel_price)
            customer.go_home()
            print(
                f"{customer.name} now has "
                f"{format_price(customer.money)} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
