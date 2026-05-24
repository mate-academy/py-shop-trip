import os
import json
import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "config.json")
    with open(config_path, "r") as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config_data["customers"]]
    shops = [Shop(**shop) for shop in config_data["shops"]]

    for index, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        best_shop = None
        cheapest_trip_cost = float("inf")
        saved_products_cost = 0

        home_location = list(customer.location)

        for shop in shops:
            if not all(
                product in shop.products
                for product in customer.product_cart
            ):
                continue

            distance = (
                (shop.location[0] - home_location[0]) ** 2
                + (shop.location[1] - home_location[1]) ** 2
            ) ** 0.5

            fuel_cost = (
                2 * distance * customer.car.fuel_consumption / 100
            ) * fuel_price
            products_cost = shop.get_products_cost(customer.product_cart)

            total_trip_cost = round(fuel_cost + products_cost, 2)

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_trip_cost:.2f}"
            )

            if total_trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = total_trip_cost
                best_shop = shop
                saved_products_cost = products_cost

        if best_shop and customer.money >= cheapest_trip_cost:
            print(f"{customer.name} rides to {best_shop.name}\n")

            customer.location = list(best_shop.location)
            current_time = datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            print(f"Date: {current_time}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():
                product_price = best_shop.products[product]
                cost = product_price * quantity

                if cost == int(cost):
                    cost = int(cost)

                name_plural = f"{product}s" if quantity > 1 else product
                print(f"{quantity} {name_plural} for {cost} dollars")

            if saved_products_cost == int(saved_products_cost):
                saved_products_cost = int(saved_products_cost)
            print(f"Total cost is {saved_products_cost} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            customer.location = home_location
            customer.money -= cheapest_trip_cost
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )

        if index < len(customers) - 1:
            print()
