import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(customer) for customer in data["customers"]]
    shops = [Shop(shop) for shop in data["shops"]]

    for customer in customers:
        trip_costs = []
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            trip_costs.append((shop, trip_cost))

        trip_costs.sort(key=lambda x: x[1])

        if trip_costs and customer.money >= trip_costs[0][1]:
            print(f"\n{customer.name} has {customer.money} dollars")
            for shop, cost in trip_costs:
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {cost:.2f}")
            shop, cost = trip_costs[0]
            print(f"{customer.name} rides to {shop.name}")
            customer.location = shop.location
            customer.make_purchase(shop)
            customer.return_home()
        else:
            for shop, cost in trip_costs:
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {cost:.2f}")
            print(f"\n{customer.name} has {customer.money} dollars")
            print(f"{customer.name} doesn't have enough money to "
                  f"make a purchase in any shop")
