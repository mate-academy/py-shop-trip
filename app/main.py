import json

from app.customer import Customer
from app.shop import Shop
from app.fuel import Fuel
from app.car import Car


def shop_trip():
    with open("app/config.json", "r") as file:
        parsed_file = json.load(file)

    Fuel.FUEL_PRICE = parsed_file["FUEL_PRICE"]

    customers = []
    for customer in parsed_file["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(customer["car"])
            )
        )

    shops = []
    for shop in parsed_file["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        lowest_price = None
        customer.shop_to_go = None

        for shop in shops:
            # calculate trip distance and price
            distance = customer.distance_to(shop.location)
            trip_price = customer.car.trip_price(distance)
            # calculate price for products
            products_price = \
                shop.calculate_price_for_cart(customer.product_cart)
            # total price
            total_price = trip_price + products_price
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_price}")

            if lowest_price is None or total_price < lowest_price:
                lowest_price = total_price
                customer.shop_to_go = shop
                customer.trip_price_for_current_shopping = trip_price

        if customer.money < lowest_price:
            print(f"{customer.name} "
                  f"doesn't have enough money to make purchase in any shop")
            continue

        customer.go_to_shop(customer.shop_to_go)

        customer.go_home()

        print(f"{customer.name} now has {customer.money} dollars\n")
