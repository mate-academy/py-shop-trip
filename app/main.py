import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in config["shops"]
    ]

    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=customer["car"]["brand"],
                fuel_consumption=customer["car"]["fuel_consumption"]
            )
        )
        for customer in config["customers"]
    ]

    for index, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            trip_costs[shop] = trip_cost
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(trip_cost, 2)}"
            )

        cheapest_shop = min(trip_costs, key=trip_costs.get)
        cheapest_trip_cost = trip_costs[cheapest_shop]

        if customer.money >= cheapest_trip_cost:
            customer.ride_to_shop(cheapest_shop)

            print()
            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart
            )
            print()

            customer.money -= cheapest_trip_cost

            customer.ride_home()
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        if index != len(customers) - 1:
            print()
