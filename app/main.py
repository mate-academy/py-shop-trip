import datetime
import json
from pathlib import Path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, "r") as f:
        config = json.load(f)

    customers = [Customer(data) for data in config["customers"]]
    shops = [Shop(data) for data in config["shops"]]
    fuel_price = config["FUEL_PRICE"]

    for index, customer in enumerate(customers):
        if index > 0:
            print()

        print(f"{customer.name} has {customer.money} dollars")

        min_total_cost = 1000000.0
        best_shop = None
        best_shop_costs = {}

        for shop in shops:
            distance = (
                (customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2
            ) ** 0.5
            price_ride = (
                customer.car.fuel_consumption / 100
                * distance
                * fuel_price
            )

            shop_costs = customer.calculate_shopping_costs(shop)
            current_total_cost = (price_ride * 2) + shop_costs["total"]

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {current_total_cost:.2f}"
            )

            if current_total_cost < min_total_cost:
                min_total_cost = current_total_cost
                best_shop = shop
                best_shop_costs = shop_costs

        if min_total_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            customer.location = best_shop.location
            customer.money -= min_total_cost

            date_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"{customer.name} rides to {best_shop.name}\n")
            print(f"Date: {date_str}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():
                cost = best_shop_costs[product]
                formatted_cost = (
                    int(cost) if cost.is_integer() else cost
                )
                print(
                    f"{quantity} {product}s for {formatted_cost} dollars"
                )

            total_cost = best_shop_costs["total"]
            formatted_total = (
                int(total_cost) if total_cost.is_integer() else total_cost
            )
            print(f"Total cost is {formatted_total} dollars")

            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
