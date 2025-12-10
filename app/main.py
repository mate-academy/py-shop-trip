import json
from app.customer import Customer
from app.shop import Shop


def shop_trip(file_name: str = "app/config.json") -> None:
    with open(file_name, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_costs = []

        for shop in shops:
            cost = customer.total_trip_cost(shop, fuel_price)
            if cost == float("inf"):
                continue
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {cost:.2f}")
            shop_costs.append((cost, shop))

        if not shop_costs:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop")
            continue

        shop_costs.sort(key=lambda x: x[0])
        cheapest_cost, cheapest_shop = shop_costs[0]

        if cheapest_cost > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop")
        else:
            customer.visit_shop(cheapest_shop, fuel_price)
