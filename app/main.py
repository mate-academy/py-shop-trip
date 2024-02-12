import os
import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    path_file = os.path.dirname(__file__)
    full_path = os.path.join(path_file, "config.json")

    with open(full_path) as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in data.get("customers")]
    shops = [Shop(**shop) for shop in data.get("shops")]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}

        for shop in shops:
            distance = customer.find_distance(shop.location)
            fuel_cost = customer.car.cost_trip(distance, fuel_price)
            product_cost = shop.calculate_product_cost(customer.product_cart)

            total_cost = fuel_cost * 2 + product_cost
            trip_costs[shop] = total_cost

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(total_cost, 2)}")

        min_cost_shop = min(trip_costs, key=trip_costs.get)

        if customer.money >= min(trip_costs.values()):
            print(f"{customer.name} rides to {min_cost_shop.name}\n")

            customer.make_order(min_cost_shop)
            print(f"\n{customer.name} rides home")
            customer.money -= min(trip_costs.values())
            print(f"{customer.name} now "
                  f"has {round(customer.money, 2)} dollars\n")

        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
