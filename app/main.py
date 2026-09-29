import json
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_path = Path(__file__).parent / "config.json"

    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
        )
        for customer in config["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        )
        for shop in config["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money:g} dollars")

        home_location = customer.location.copy()
        trip_costs = []

        for shop in shops:
            if not customer.can_buy_from(shop):
                continue

            cost = customer.cost_of_the_trip(
                shop,
                fuel_price,
            )

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {cost:.2f}"
            )

            trip_costs.append((cost, shop))

        affordable_trips = [
            (cost, shop)
            for cost, shop in trip_costs
            if cost <= customer.money
        ]

        if not affordable_trips:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        cheapest_cost, cheapest_shop = min(
            affordable_trips,
            key=lambda trip: trip[0],
        )

        print(
            f"{customer.name} rides to "
            f"{cheapest_shop.name}\n"
        )

        customer.location = cheapest_shop.location.copy()

        cheapest_shop.buy_products(
            customer.product_cart,
            customer.name,
        )

        customer.money -= cheapest_cost

        customer.location = home_location

        print(f"{customer.name} rides home")

        print(
            f"{customer.name} now has "
            f"{customer.money:.2f} dollars\n"
        )


if __name__ == "__main__":
    shop_trip()
