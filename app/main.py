import json
from typing import List
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    customers_data: List[dict] = config["customers"]
    shops_data: List[dict] = config["shops"]

    shops = [Shop(s["name"], s["location"], s["products"]) for s in shops_data]

    for cust in customers_data:
        customer = Customer(
            cust["name"],
            cust["product_cart"],
            cust["location"],
            cust["money"],
            cust["car"],
        )

        print(f"{customer.name} has {round(customer.money, 2)} dollars")

        trip_costs = []
        for shop in shops:
            cost = shop.trip_cost(customer, fuel_price)
            trip_costs.append((cost, shop))
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{round(cost, 2)}"
            )

        cheapest_cost, cheapest_shop = min(trip_costs, key=lambda x: x[0])

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money to make a "
                "purchase in any shop"
            )
            continue

        print(f"{customer.name} rides to {cheapest_shop.name}")
        customer.go_to(cheapest_shop.location)

        cheapest_shop.print_receipt(customer)

        customer.money -= cheapest_cost

        print(f"{customer.name} rides home")
        customer.go_home()

        print(f"{customer.name} now has {round(customer.money, 2)} dollars")
        print()
