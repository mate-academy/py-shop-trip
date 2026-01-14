import json
import os
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(current_file_path))
    config_path = os.path.join(project_root, "config.json")

    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**shop) for shop in config["shops"]]
    customers = []

    for data in config["customers"]:
        car_data = data.pop("car")
        car = Car(**car_data)
        customer = Customer(car=car, **data)
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            trip_costs[shop] = cost
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(cost, 2)}")

        cheapest_shop, cheapest_cost = min(trip_costs.items(),
                                           key=lambda item: item[1]
                                           )

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.go_to(cheapest_shop.location)

            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart
            )
            customer.money -= cheapest_cost
            print(f"{customer.name} rides home")
            customer.go_to(config["customers"][0]["location"])
            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
