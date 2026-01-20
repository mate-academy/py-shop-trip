import os
import json
import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    # Load configuration
    config_path = os.path.join("app", "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    # Initialize shops
    shops = [Shop(shop["name"], shop["location"],
                  shop["products"]) for shop in shops_data]

    # Process each customer
    for customer_data in customers_data:
        car = Car(customer_data["car"]["brand"],
                  customer_data["car"]["fuel_consumption"])
        customer = Customer(customer_data["name"],
                            customer_data["product_cart"],
                            customer_data["location"],
                            customer_data["money"], car)

        print(f"{customer.name} has {customer.money} dollars")

        # Calculate trip costs for each shop
        trip_options = []
        for shop in shops:
            distance_to_shop = customer.calculate_distance(shop.location)
            distance_to_home = distance_to_shop
            fuel_cost = car.calculate_fuel_cost(
                distance_to_shop + distance_to_home, fuel_price)
            cart_cost = shop.calculate_cart_cost(customer.product_cart)

            if cart_cost is not None:
                total_trip_cost = fuel_cost + cart_cost
                trip_options.append((shop, total_trip_cost,
                                     fuel_cost, cart_cost))

        # Output trip costs for each shop
        for option in trip_options:
            shop, total_cost, fuel_cost, cart_cost = option
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs{total_cost: .2f}")

        # Choose the cheapest option
        trip_options.sort(key=lambda option: option[1])

        if trip_options and customer.has_enough_money(trip_options[0][1]):
            chosen_shop, total_cost, fuel_cost, cart_cost = trip_options[0]

            total_cost = round(total_cost, 2)
            fuel_cost = round(fuel_cost, 2)
            cart_cost = round(cart_cost, 2)

            print(f"{customer.name} rides to {chosen_shop.name}\n")

            # Print the receipt with the correct date format
            print(
                f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            )
            chosen_shop.print_receipt(customer.name,
                                      customer.product_cart, cart_cost)

            customer.update_location(customer_data["location"])
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f"{round(customer.money - total_cost, 2): .2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
