import os
import json
from datetime import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    # Try multiple locations to find the config file
    possible_paths = [
        # First try direct path
        "config.json",
        # Try from current directory
        os.path.join(os.getcwd(), "config.json"),
        # Try from the app directory
        os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "config.json"),
        # Try from one level up (project root)
        os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), "config.json"),
    ]

    config_path = None
    for path in possible_paths:
        if os.path.exists(path):
            config_path = path
            break

    if not config_path:
        raise FileNotFoundError("Could not "
                                "find config.json in any expected location")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]

    # Create shop objects from config
    shops = []
    for shop_data in config["shops"]:
        shops.append(Shop(
            name=shop_data["name"],
            location=shop_data["location"],
            products=shop_data["products"]  # Changed to match JSON key
        ))

    # Create customer objects from config
    customers = []
    for customer_data in config["customers"]:
        car_data = customer_data["car"]
        car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"],
            location=customer_data["location"]  # Car uses customer's location
        )
        customer = Customer(
            name=customer_data["name"],
            money=customer_data["money"],
            location=customer_data["location"],
            car=car,
            product_cart=customer_data["product_cart"]
        )
        customers.append(customer)

    # Process each customer's shopping trip
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_total_cost = float("inf")
        chosen_shop = None
        product_cost_at_chosen_shop = 0

        for shop in shops:
            distance = customer.distance_to(shop.location)
            trip_cost = customer.car.cost_for_road(distance * 2, fuel_price)
            product_cost = shop.calculate_cart_cost(customer.product_cart)
            total_cost = trip_cost + product_cost

            print(f"{customer.name}'s "
                  f"trip to the {shop.name} costs {round(total_cost, 2)}")

            if total_cost < min_total_cost:
                min_total_cost = total_cost
                chosen_shop = shop
                product_cost_at_chosen_shop = product_cost

        if chosen_shop and customer.money >= min_total_cost:
            print(f"{customer.name} rides to {chosen_shop.name}\n")

            # Customer arrives at the shop
            customer.location = chosen_shop.location

            chosen_shop.print_receipt(
                current_time=datetime(
                    2021, 1, 4, 12, 33, 41).strftime(
                    "%d/%m/%Y %H:%M:%S"),
                cust_name=customer.name,
                total_cost=product_cost_at_chosen_shop,
                cart=customer.product_cart
            )

            # Customer returns home
            print(f"\n{customer.name} rides home")
            customer.money -= min_total_cost
            print(f"{customer.name} now "
                  f"has {round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't "
                  f"have enough money to make a purchase in any shop")
