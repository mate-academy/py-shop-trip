import json

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    data = None

    with open("./app/config.json", "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]
    customers = tuple(
        Customer(
            name=customer_data["name"],
            product_cart=customer_data["product_cart"],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(**customer_data["car"])
        )
        for customer_data in data["customers"]
    )
    shops = tuple(Shop(**shop_data) for shop_data in data["shops"])

    for customer_ in customers:
        trips_costs: dict[float, Shop] = {}

        customer_.print_money_info()

        for shop in shops:

            distance = customer_.get_distance(shop)
            fuel_needed = customer_.get_fuel_needed(distance)
            fuel_cost = customer_.get_fuel_cost(fuel_needed, fuel_price)
            purchase_cost = shop.get_purchase_cost(customer_)
            cost_trip = customer_.get_cost_trip(purchase_cost, fuel_cost)
            trips_costs[cost_trip] = shop
            customer_.print_trip_info(cost_trip, shop.name)

        cheapest_cost = min(trips_costs)

        if cheapest_cost < customer_.money:
            cheapest_shop = trips_costs[cheapest_cost]

            customer_.print_ride_shop(cheapest_shop.name)

            purchase_cost = cheapest_shop.get_purchase_cost(customer_)
            cheapest_shop.print_purchase_info(customer_, purchase_cost)

            customer_.money -= cheapest_cost
            print(f"{customer_.name} rides home")
            customer_.print_money_info(after_purchase=True)
        else:
            print(
                f"{customer_.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )
