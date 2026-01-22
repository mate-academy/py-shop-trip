import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(shop_data["name"], shop_data["location"], shop_data["products"])
        for shop_data in config["shops"]
    ]

    customers = []
    for cust_data in config["customers"]:
        car_data = cust_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customer = Customer(
            cust_data["name"],
            cust_data["product_cart"],
            cust_data["location"],
            cust_data["money"],
            car,
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}
        for shop in shops:
            fuel_cost = customer.calculate_trip_cost(shop, fuel_price)

            try:
                product_cost = shop.calculate_product_cost(
                    customer.product_cart
                )
            except KeyError:
                continue

            total_cost = round(fuel_cost + product_cost, 2)
            trip_costs[shop] = total_cost
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total_cost}"
            )

        affordable_shops = {
            shop: cost for shop, cost in trip_costs.items()
            if customer.can_afford(cost)
        }

        if not affordable_shops:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        chosen_shop = min(affordable_shops, key=affordable_shops.get)
        total_cost = affordable_shops[chosen_shop]

        print(f"{customer.name} rides to {chosen_shop.name}")
        customer.travel_to(chosen_shop.location)

        chosen_shop.print_receipt(customer.name, customer.product_cart)

        customer.pay(total_cost)

        customer.travel_to(customer.home_location)
        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
