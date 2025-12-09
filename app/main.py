import datetime
import json
from pathlib import Path
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = Path(__file__).resolve().parent
    config_path = current_dir.parent / "config.json"
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops : list[Shop] = []
    for shop_data in config["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"],
        )
        shops.append(shop)

    customers: list[Customer] = []
    for customer_data in config["customers"]:
        car = Car(
            brand=customer_data["car"]["brand"],
            fuel_consumption=customer_data["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=car
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = float("inf")
        cheapest_cart = 0

        for shop in shops:
            distance = customer.distance_to(shop.location)
            fuel_cost = customer.car.fuel_needed(distance) * fuel_price

            shop_cost = shop.get_total_cost(customer.product_cart)

            total = shop_cost + (fuel_cost * 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total:.2f}")

            if total < cheapest_cost:
                cheapest_cost = total
                cheapest_shop = shop
                cheapest_cart = shop_cost

        if cheapest_cost > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            home = customer.location
            customer.move_to(cheapest_shop.location)
            customer.purchase(cheapest_cost)
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            for product, quantity in customer.product_cart.items():
                price = cheapest_shop.products[product] * quantity
                print(f"{quantity} {product}s for "
                      f"{price:.2f}".rstrip("0").strip(".") + " dollars")

            print(f"Total cost is {cheapest_cart} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            customer.move_to(home)
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
