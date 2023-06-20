import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config = json.load(config_file)

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
                config["FUEL_PRICE"]
            )
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

    customer_trip = ""

    for customer in customers:
        customer_trip += f"{customer.name} has {customer.money} dollars\n"
        (
            trip_prices,
            selected_shop,
            min_total_cost
        ) = customer.find_the_cheapest_trip(shops)
        customer_trip += trip_prices

        if customer.money >= min_total_cost:
            customer_trip += customer.ride_to_shop(selected_shop)
            customer_trip += selected_shop.buy_products(customer)
            customer_trip += customer.ride_home()

        else:
            customer_trip += (
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop\n\n"
            )

    print(customer_trip[:-2])
