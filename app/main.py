import json

import datetime

from app.shop import Shops

from app.customer import Customers


def cost_fuel_calculate(
        customer_location: list[int],
        shop_location: list,
        fuel_price: float,
        fuel_cons: float
) -> float:
    distance = ((shop_location[0] - customer_location[0]) ** 2
                + (shop_location[1] - customer_location[1]) ** 2) ** 0.5

    sum_cost_fuel = (fuel_cons / 100) * (distance * 2) * fuel_price

    return sum_cost_fuel


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_cost = data["FUEL_PRICE"]
    min_cost = {}

    for customer in data["customers"]:
        counter = 0
        total_cost = 0

        customer = Customers(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"])
        print(f"{customer.name} has {customer.money} dollars")

        customer_home = customer.location

        for shop in data["shops"]:
            current_shop_food_cost = 0
            shops = Shops(
                shop["name"],
                shop["location"],
                shop["products"]
            )

            fuel = cost_fuel_calculate(
                customer_location=customer.location,
                shop_location=shops.location,
                fuel_price=fuel_cost,
                fuel_cons=customer.car["fuel_consumption"]
            )

            for key in customer.product_cart.keys():
                current_shop_food_cost += \
                    customer.product_cart[key] * shops.products[key]

            total_cost = fuel + current_shop_food_cost

            min_cost.update({shops.name: total_cost})

            print(
                f"{customer.name}'s trip to the "
                f"{shops.name} costs {total_cost:.2f}")

        if customer.money > total_cost:
            low_cost_shop_name = min(min_cost, key=min_cost.get)

            print(f"{customer.name} rides to {low_cost_shop_name}\n")

            customer.location = shops.location

            current_datetime = datetime.datetime.now()

            print(
                f"Date: {current_datetime.strftime('%d/%m/%Y %H:%M:%S')}")

            print(f"Thanks, {customer.name}, for your purchase!")

            print("You have bought:")

            selected_shop_data = next(
                shop for shop in data["shops"]
                if shop["name"] == low_cost_shop_name)

            for key, value in selected_shop_data["products"].items():
                product_cost = customer.product_cart.get(key) * value
                counter += product_cost

                print(
                    f"{customer.product_cart.get(key)} {key}s for "
                    f"{'%g' % product_cost} dollars")

            print(f"Total cost is {counter} dollars")

            print("See you again!\n")

            print(f"{customer.name} rides home")

            customer.location = customer_home

            print(f"{customer.name} now has "
                  f"{customer.money - min_cost.get(selected_shop_data.get('name')):.2f}"
                  f" dollars\n")

        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop")
