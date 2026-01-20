import json
from pathlib import Path
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"
    with config_path.open() as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(sh["name"],
             sh["location"],
             sh["products"]) for sh in config["shops"]]

    customers = []
    for cust in config["customers"]:
        car = Car(cust["car"]["brand"], cust["car"]["fuel_consumption"])
        customers.append(Customer(
            cust["name"],
            cust["product_cart"],
            cust["location"],
            cust["money"],
            car)
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = [
            (shop, customer.trip_cost(shop, fuel_price)) for shop in shops
        ]
        for shop, cost in trip_costs:
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")

        cheapest_shop, cheapest_cost = min(trip_costs, key=lambda x: x[1])
        if customer.money >= cheapest_cost:
            customer.go_shopping(cheapest_shop, cheapest_cost)
        else:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
