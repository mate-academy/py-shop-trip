import json
import datetime

from app.point import Point
from app.spending import Spending


def print_receipt(customer: dict, shop: dict | None, pure_cost: float) -> None:
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Date: {current_time}")
    print(f"Thanks, {customer['name']}, for your purchase!")
    print("You have bought:")

    for product, qty in customer["product_cart"].items():
        price_per_item = shop["products"][product]
        prod_total = qty * price_per_item
        if isinstance(prod_total, float) and prod_total.is_integer():
            prod_total = int(prod_total)
        print(f"{qty} {product}s for {prod_total} dollars")

    if isinstance(pure_cost, float) and pure_cost.is_integer():
        pure_cost = int(pure_cost)

    print(f"Total cost is {pure_cost} dollars")
    print("See you again!\n")


def shop_trip() -> None:
    with open("./app/config.json", "r") as json_file:
        config = json.load(json_file)

    customers = config["customers"]

    for i, customer in enumerate(customers):
        print(f"{customer['name']} has {customer['money']} dollars")

        customer_point = Point(*customer["location"])
        spending = Spending(
            config["FUEL_PRICE"],
            customer["car"]["fuel_consumption"]
        )

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in config["shops"]:
            shop_point = Point(*shop["location"])
            dist = customer_point.distance_to_point(shop_point)
            fuel_cost = spending.calculate_fuel_costs(dist)
            product_cost = spending.calculate_product_costs(
                customer["product_cart"], shop["products"]
            )
            total_cost = fuel_cost + product_cost

            print(
                f"{customer['name']}'s trip to the {shop['name']} "
                f"costs {total_cost:.2f}"
            )

            if total_cost < min_trip_cost:
                min_trip_cost = total_cost
                cheapest_shop = shop

        if customer["money"] >= min_trip_cost:
            shop_name = cheapest_shop["name"]
            print(f"{customer['name']} rides to {shop_name}\n")

            customer["location"] = cheapest_shop["location"]

            pure_product_cost = spending.calculate_product_costs(
                customer["product_cart"], cheapest_shop["products"]
            )

            print_receipt(customer, cheapest_shop, pure_product_cost)

            print(f"{customer['name']} rides home")
            remaining_money = customer["money"] - min_trip_cost
            print(f"{customer['name']} now has {remaining_money:.2f} dollars")
        else:
            print(
                f"{customer['name']} doesn't have enough "
                f"money to make a purchase in any shop"
            )

        if i < len(customers) - 1:
            print()
