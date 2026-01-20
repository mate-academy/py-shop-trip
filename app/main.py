import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
    for customer in data["customers"]:
        customer_actually = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"]
        )
        customer_car = Car(
            data["FUEL_PRICE"],
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        customer_actually.start_customer()
        cheapest_shop = None
        for shop in data["shops"]:
            actually_shop = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            fuel_cost = customer_car.cost_fuel_to_shop(
                customer_actually.location,
                actually_shop.location
            )
            if (
                cheapest_shop is None
                or cheapest_shop[0] > actually_shop.costs_trip(
                    fuel_cost, customer_actually.product_cart
                )
            ):
                cheapest_shop = (
                    actually_shop.costs_trip(
                        fuel_cost, customer_actually.product_cart
                    ),
                    actually_shop
                )
            trip_cost = round(
                actually_shop.costs_trip(
                    fuel_cost, customer_actually.product_cart
                ), 2
            )
            print(f"{customer_actually.name}'s trip to "
                  f"the {actually_shop.name} costs {trip_cost}")
        full_prices = cheapest_shop[0]
        shop = cheapest_shop[1]
        if full_prices <= customer_actually.money:
            customer_actually.start_ride_to_shop(shop)
            shop.customer_in_magazine(
                customer_actually.name,
                customer_actually.product_cart
            )
            customer_actually.end_trip(full_prices)
        else:
            print(f"{customer_actually.name} doesn't have "
                  f"enough money to make a purchase in any shop")
