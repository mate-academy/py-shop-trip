import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    data = json.load(open("app/config.json"))
    customers = [
        Customer(
            name=person["name"],
            product_cart=person["product_cart"],
            location=person["location"],
            money=person["money"],
            car=Car(
                person["car"]["brand"],
                person["car"]["fuel_consumption"]
            )
        )
        for person in data["customers"]
    ]

    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in data["shops"]
    ]

    for customer in customers:
        print(customer)

        trip_costs = []
        for shop in shops:
            fuel_cost = customer.trip_costs(shop)
            products_cost = shop.calculate_cart_cost(customer.product_cart)
            total_cost = fuel_cost + products_cost
            trip_costs.append((shop, total_cost))
            print(customer.trip_costs_announcer(shop))

        cheapest_shop, cheapest_cost = min(
            trip_costs, key=lambda money: money[1]
        )

        if customer.money >= cheapest_cost:
            print(
                customer.go_to_shop(
                    cheapest_shop.name
                )
            )
            print()
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            customer.money = round(customer.money - cheapest_cost, 2)
            print()
            print(customer.go_home())
            print(f"{customer.name} now has {customer.money} dollars")
            print()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
