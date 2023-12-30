import json

import datetime

from app.shop import Shops

from app.customer import Customers


def cost_fuel_calculate(
        customer_location: list,
        shop_location: list,
        fuel_price: float,
        fuel_cons: float
) -> float:
    distance = ((shop_location[0] - customer_location[0]) ** 2
                + (shop_location[1] - customer_location[1]) ** 2) ** 0.5

    sum_cost_fuel = (fuel_cons / 100) * (distance * 2) * fuel_price

    return sum_cost_fuel


def cost_food(product_chart: dict, product: dict) -> dict:
    price_milk = product_chart.get("milk") * product.get("milk")
    price_bread = product_chart.get("bread") * product.get("bread")
    price_butter = product_chart.get("butter") * product.get("butter")
    return {
        "milk_cost": price_milk,
        "bread_cost": price_bread,
        "butter_cost": price_butter}


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        fuel_cost = data["FUEL_PRICE"]
        min_cost = {}

        for customer in data["customers"]:
            customer = Customers(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"])
            print(f"{customer.name} has {customer.money} dollars")

            customer_home = customer.location

            for shop in data["shops"]:
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

                food_cost = cost_food(customer.product_cart, shops.products)

                total_cost = (fuel + food_cost.get("milk_cost")
                              + food_cost.get("bread_cost")
                              + food_cost.get("butter_cost"))

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

                selected_shop = Shops(
                    selected_shop_data["name"],
                    selected_shop_data["location"],
                    selected_shop_data["products"])

                milk = customer.product_cart.get(
                    "milk") * selected_shop.products.get("milk")
                bread = customer.product_cart.get(
                    "bread") * selected_shop.products.get("bread")
                butter = customer.product_cart.get(
                    "butter") * selected_shop.products.get("butter")

                print(
                    f"{customer.product_cart.get('milk')} "
                    f"milks for {milk} dollars"
                )

                print(
                    f"{customer.product_cart.get('bread')} "
                    f"breads for {round(bread)} dollars")

                print(
                    f"{customer.product_cart.get('butter')} "
                    f"butters for {butter} dollars")

                print(f"Total cost is {milk + bread + butter} dollars")

                print("See you again!\n")

                print(f"{customer.name} rides home")

                customer.location = customer_home

                print(
                    f"{customer.name} now has "
                    f"{customer.money - min_cost.get(selected_shop.name):.2f} "
                    f"dollars\n")

            else:
                print(
                    f"{customer.name} doesn't have enough money "
                    f"to make a purchase in any shop")
