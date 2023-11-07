import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
    fuel_price = data.get("FUEL_PRICE")
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        customer.money_count()

        trips_prices = []
        for shop in shops:

            fuel_expenses = customer.car.calculate_fuel_expenses(
                customer.calculate_distance(shop.location),
                fuel_price
            )
            trip_cost = shop.calculate_trip_cost(
                shop.calculate_product_cost(customer),
                fuel_expenses)
            trips_prices.append(trip_cost)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(trip_cost, 2)}")

        shop_index = trips_prices.index(min(trips_prices))
        shop = shops[shop_index]

        if min(trips_prices) > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        purchases = shop.calculate_product_cost(customer)
        print(f"{customer.name} rides to {shop.name}\n")
        customer.location = shop.location
        shop.generate_receipt(customer, purchases)
        customer.location = customer.home_location
        print(f"\n{customer.name} rides home"
              f"\n{customer.name} now has "
              f"{round(customer.money - min(trips_prices), 2)} dollars\n")
