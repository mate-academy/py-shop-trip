import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]

    customers = []
    for customer in customers_data:
        car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )

        new_customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            car
        )

        customers.append(new_customer)

    shops = [Shop(shop["name"], shop["location"], shop["products"])
             for shop in shops_data]

    for customer in customers:
        cheapest_shop = None
        cheapest_price = float("inf")

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = shop.calculate_trip_cost(customer, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost:.2f}")

            if trip_cost < cheapest_price and trip_cost <= customer.money:
                cheapest_price = trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            cheapest_shop.make_purchase(customer)
            customer.return_home(cheapest_shop.location, fuel_price)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
