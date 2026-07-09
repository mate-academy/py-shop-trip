from pathlib import Path
import json
import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    config_path = Path(__file__).resolve().parent.parent / "config.json"
    with (open(config_path, "r") as f):
        config = json.load(f)
        customers = [Customer.from_config(c) for c in config["customers"]]
        shops = [Shop.from_config(s) for s in config["shops"]]

        for customer in customers:
            shop_costs = {}
            cheapest_shop = None
            cheapest_price = float("inf")
            original_location = customer.location

            for shop in shops:
                distance = (
                    (shop.location[0] - customer.location[0]) ** 2
                    + (shop.location[1] - customer.location[1]) ** 2
                ) ** 0.5
                fuel_to_shop = (
                    distance
                    * customer.car.fuel_consumption
                    / 100
                    * config["FUEL_PRICE"]
                )
                fuel_back = fuel_to_shop

                products_cost = 0
                for product, quantity in customer.product_cart.items():
                    price = shop.products[product]
                    products_cost += quantity * price
                total_trip_cost = round(
                    (fuel_to_shop + products_cost + fuel_back),
                    2)
                shop_costs[shop.name] = total_trip_cost

                if total_trip_cost < cheapest_price:
                    cheapest_price = total_trip_cost
                    cheapest_shop = shop

            print(f"{customer.name} has {customer.money} dollars")

            for shop, price in shop_costs.items():
                print(f"{customer.name}'s trip "
                      f"to the {shop} costs {price}")

            if customer.money >= cheapest_price:
                print(f"{customer.name} rides to {cheapest_shop.name}")
                customer.location = cheapest_shop.location

                print("")
                print(
                    f"Date: "
                    f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                )
                print(f"Thanks, {customer.name}, for your purchase!")
                print("You have bought:")

                total_price = 0
                for product, quantity in customer.product_cart.items():
                    price = cheapest_shop.products[product]
                    total = price * quantity
                    if total.is_integer():
                        total = int(total)
                    total_price += total
                    print(f"{quantity} {product}s for {total} dollars")
                print(f"Total cost is {total_price} dollars")
                print("See you again!")
                print("")
                print(f"{customer.name} rides home")
                customer.money -= cheapest_price
                customer.location = original_location
                print(f"{customer.name} now has {customer.money} dollars")
                print("")
            else:
                print(
                    f"{customer.name} doesn't have "
                    f"enough money to make a purchase in any shop")
