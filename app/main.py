# app/main.py

import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    """Main function to calculate and execute
     the cheapest trip for customers."""
    with open("config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = []
    shops = []

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

    for shop_data in config["shops"]:
        shop = Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_trip_cost = float("inf")
        cheapest_shop = None

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name}"
                  f" costs {trip_cost}")
            if trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.make_purchase(cheapest_shop, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
