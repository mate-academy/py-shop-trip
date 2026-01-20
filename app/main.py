import json

from datetime import datetime

from app.customer.customer import Customer
from app.car.car import Car
from app.shop.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as json_file:
        data = json.load(json_file)

    fuel_price = data.get("FUEL_PRICE")
    customers = data.get("customers")
    shops = data.get("shops")

    shop_instances = []

    for shop in shops:
        new_shop = Shop(
            name=shop.get("name"),
            location=shop.get("location"),
            products=shop.get("products")
        )
        shop_instances.append(new_shop)

    for person in customers:
        car = Car(
            brand=person["car"]["brand"],
            fuel_consumption=person["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=person.get("name"),
            product_cart=person.get("product_cart"),
            location=person.get("location"),
            money=person.get("money"),
            car=car
        )

        print(f"{customer.name} has {customer.money} dollars")

        shop, trip_cost = customer.find_cheapest_trip(
            shop_instances,
            fuel_price
        )

        if customer.money >= trip_cost:

            print(f"{customer.name} rides to {shop.name}\n")
            date = datetime(2021, 1, 4, 12, 33, 41).strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")

            total_cost = 0
            for product, amount in customer.product_cart.items():
                cost = amount * shop.products.get(product)
                print(f"{amount} {product}s for {cost} dollars")
                total_cost += cost

            print(f"Total cost is {total_cost} dollars\nSee you again!")
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money - trip_cost, 2)} dollars\n")
            continue

        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
