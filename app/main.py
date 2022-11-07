import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)

        fuel_price = info["FUEL_PRICE"]

        shops = [Shop(
            shop["name"],
            shop["location"],
            shop["products"])
            for shop in info["shops"]]

        customers = [Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"],
                customer["car"]["fuel_consumption"]))
            for customer in info["customers"]]

        for customer in customers:
            customer.balance_printer()

            for shop, trip_price in customer.total_cost(
                    shops, fuel_price).items():
                print(f"{customer.name}'s trip to the"
                      f" {shop} costs {trip_price}")

            min_trip = customer.best_trip(shops, fuel_price)

            if customer.total_cost(shops,
                                   fuel_price)[min_trip] >= customer.money:
                print(f"{customer.name}"
                      f" doesn't have enough money to make "
                      f"purchase in any shop")
            else:
                print(f"{customer.name} rides to {min_trip}\n")

                for shop in shops:
                    if shop.name == min_trip:
                        shop.print_check(customer)

                print(f"\n{customer.name} rides home")
                print(f"{customer.name} now has"
                      f" {customer.new_balance(shops, fuel_price, min_trip)}"
                      f" dollars\n")
