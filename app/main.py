import json
import math
import datetime


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    def distance(
            loc1: tuple[float, float],
            loc2: tuple[float, float]
    ) -> float:
        return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    for customer in config["customers"]:
        name = customer["name"]
        location = customer["location"]
        money = customer["money"]
        fuel_consumption = customer["car"]["fuel_consumption"]
        product_cart = customer["product_cart"]

        print(f"{name} has {money} dollars")

        trip_costs = []
        for shop in config["shops"]:
            shop_name = shop["name"]
            shop_location = shop["location"]
            products = shop["products"]

            dist_to_shop = distance(location, shop_location)
            dist_home = distance(shop_location, location)

            fuel_to_shop = (dist_to_shop / 100) * fuel_consumption * fuel_price
            fuel_home = (dist_home / 100) * fuel_consumption * fuel_price

            products_cost = sum(
                products[p] * q for p,
                q in product_cart.items() if p in products
            )

            total_cost = round(fuel_to_shop + fuel_home + products_cost, 2)
            trip_costs.append((total_cost, shop))
            print(f"{name}'s trip to the {shop_name} costs {total_cost}")

        cheapest_cost, cheapest_shop = min(trip_costs, key=lambda x: x[0])

        if cheapest_cost > money:
            print(
                f"{name} doesn't have enough money to make a purchase "
                f"in any shop"
            )
            continue

        print(f"{name} rides to {cheapest_shop['name']}")
        print()
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")

        total_products_cost = 0
        for product, qty in product_cart.items():
            price = cheapest_shop["products"][product] * qty
            total_products_cost += price
            price_str = int(price) if price.is_integer() else price
            print(f"{qty} {product}s for {price_str} dollars")

        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!")
        print()
        print(f"{name} rides home")

        remaining_money = round(money - cheapest_cost, 2)
        print(f"{name} now has {remaining_money} dollars")
        print()
