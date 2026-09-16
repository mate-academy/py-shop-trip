import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        for customer in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = []

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(
                shop,
                fuel_price
            )

            trip_costs.append((trip_cost, shop))

        cheapest_cost, cheapest_shop = min(trip_costs)

        if customer.money >= cheapest_cost:
            print(
                f"{customer.name} rides to "
                f"{cheapest_shop.name}"
            )

            customer.go_to_shop(cheapest_shop)

            products_cost = customer.buy_products(
                cheapest_shop
            )

            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart,
                products_cost
            )

            customer.go_home()

            customer.money = customer.money - (
                cheapest_cost - products_cost
            )

            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money:.2f} dollars"
            )
            print()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
