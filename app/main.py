import os
import json
from app.shop import Shop
from app.customer import Customer


def format_number(num: float | int) -> int | float:
    return int(num) if float(num).is_integer() else num


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]

    shops = [
        Shop(shop_data["name"], shop_data["location"],
             shop_data["products"])
        for shop_data in data["shops"]
    ]

    customers = [
        Customer(
            c["name"], c["product_cart"], c["location"],
            c["money"], c["car"]
        )
        for c in data["customers"]
    ]

    for i, customer in enumerate(customers):
        print(f"{customer.name} has {format_number(customer.money)} dollars")

        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {format_number(cost)}"
            )

            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop

        if customer.money >= min_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            print(f"\n{customer.name} rides home")
            customer.money -= min_cost
            final_cash = format_number(round(customer.money, 2))
            print(f"{customer.name} now has {final_cash} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough money to "
                "make a purchase in any shop"
            )

        if i < len(customers) - 1:
            print()


if __name__ == "__main__":
    shop_trip()
