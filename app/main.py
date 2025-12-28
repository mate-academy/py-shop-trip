import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]
    customers = [
        Customer(
            name=c["name"],
            product_cart=c["product_cart"],
            location=c["location"],
            money=c["money"],
            car=Car(**c["car"])
        )
        for c in config["customers"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            total = customer.trip_cost_to(shop, fuel_price)
            costs.append((shop, total))
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {total:.2f}")
        best_shop, best_cost = min(costs, key=lambda x: x[1])
        if customer.money >= best_cost:
            print(f"{customer.name} rides to {best_shop.name}")
            customer.location = best_shop.location
            best_shop.sell_products(customer.product_cart, customer.name)
            customer.money -= best_cost
            customer.location = customer.home_location
            print(f"{customer.name} rides home")
            print(f"{customer.name} now "
                  f"has {round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
