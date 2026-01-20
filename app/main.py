import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    customers = [Customer(**cust) for cust in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop = None
        min_total_cost = float("inf")

        for shop in shops:
            distance = customer.calculate_distance(shop.location)
            fuel_trip_cost = 2 * customer.fuel_cost(distance, fuel_price)

            try:
                purchase_cost = 0
                for product, qty in customer.product_cart.items():
                    price = shop.get_product_price(product)
                    purchase_cost += price * qty
            except ValueError:
                continue

            total_cost = fuel_trip_cost + purchase_cost

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_cost:.2f}")

            if total_cost < min_total_cost:
                min_total_cost = total_cost
                best_shop = shop

        if best_shop and min_total_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}")

            total_purchase_cost = customer.buy_products(best_shop)

            distance = customer.calculate_distance(best_shop.location)
            fuel_cost_total = 2 * customer.fuel_cost(distance, fuel_price)

            customer.money -= (total_purchase_cost + fuel_cost_total)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
