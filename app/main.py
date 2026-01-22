from app.car import Car
from app.customer import Customer
from app.shop import Shop
from datetime import datetime
import json


def shop_trip() -> None:
    config = {}
    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    for customer in customers:
        car = Car(
            brand=customer["car"]["brand"],
            fuel_consumption=customer["car"]["fuel_consumption"]
        )
        customer_instance = Customer(
            name=customer["name"],
            location=customer["location"],
            products=customer["product_cart"],
            money=customer["money"],
            car=car
        )
        print(
            f"{customer_instance.name} has "
            f"{customer_instance.money} dollars"
        )
        min_cost = customer_instance.money
        cheapest_shop = Shop(
            name=shops[0]["name"],
            location=shops[0]["location"],
            products=shops[0]["products"]
        )

        for shop in shops:
            shop_instance = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            cost = customer_instance.cost_trip(
                location=shop_instance.location,
                fuel_price=fuel_price
            ) + customer_instance.cost_product(
                products=shop_instance.products
            )
            print(
                f"{customer_instance.name}'s trip "
                f"to the {shop_instance.name} costs {cost}"
            )
            if min_cost > cost:
                min_cost = cost
                cheapest_shop = shop_instance
        if min_cost < customer_instance.money:
            print(f"{customer_instance.name} rides to {cheapest_shop.name}")
            print()
            current_datetime = datetime(2021, 1, 4, 12, 33, 41)
            current_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {current_datetime}")
            print(f"Thanks, {customer_instance.name}, for your purchase!")
            print("You have bought:")

            cost_products = 0
            for product in customer_instance.products:
                cost_any_product = (
                    customer_instance.products[product]
                    * cheapest_shop.products[product]
                )
                if (cost_any_product * 10) % 10 == 0:
                    cost_any_product = int(cost_any_product)
                print(
                    f"{customer_instance.products[product]} {product}s "
                    f"for {cost_any_product} dollars"
                )
                cost_products += cost_any_product
            print(f"Total cost is {cost_products} dollars")
            print("See you again!")
            print()
            print(f"{customer_instance.name} rides home")
            print(
                f"{customer_instance.name} now has "
                f"{customer_instance.money - min_cost} dollars"
            )
            print()
        else:
            print(
                f"{customer_instance.name} doesn't have"
                f" enough money to make a purchase in any shop"
            )
