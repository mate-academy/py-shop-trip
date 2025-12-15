import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(**cust) for cust in config["customers"]]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_costs = []
        for shop in shops:
            cost = customer.trip_cost(shop, fuel_price)
            shop_costs.append((shop, cost))
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {cost:.2f}"
            )

        affordable = [
            (shop, cost) for shop, cost in shop_costs
            if customer.can_afford(cost)
        ]
        if not affordable:
            print(
                f"{customer.name} doesn't have enough money to make "
                f"a purchase in any shop\n"
            )
            continue

        best_shop, total_cost = min(affordable, key=lambda x: x[1])
        customer.complete_trip(best_shop, fuel_price, total_cost)
