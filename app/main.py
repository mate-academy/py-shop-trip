import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        initial_data = json.load(file)

    fuel_price = initial_data["FUEL_PRICE"]
    customers = [Customer(item) for item in initial_data["customers"]]
    shops = [Shop(item) for item in initial_data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            costs.append((cost, shop))
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {cost:.2f}"
            )

        cheapest_trip_cost, cheapest_shop = min(costs, key=lambda x: x[0])

        if customer.money < cheapest_trip_cost:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
        else:
            customer.drive_to_shop(cheapest_shop, cheapest_trip_cost)
