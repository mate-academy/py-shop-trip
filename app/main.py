import json

from car import Car
from customer import Customer
from shop import Shop


def shop_trip() -> None:
    with open("config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config["shops"]
    ]

    for customer_data in config["customers"]:
        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            Car(
                customer_data["car"]["brand"],
                customer_data["car"][
                    "fuel_consumption"
                ],
            ),
        )

        print(
            f"{customer.name} "
            f"has {customer.money} dollars"
        )

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            distance = customer.distance_to(
                shop.location
            )

            fuel_cost = (
                customer.car.trip_cost(
                    distance * 2,
                    fuel_price
                )
            )

            purchases_cost = (
                shop.products_cost(
                    customer.product_cart
                )
            )

            trip_cost = (
                fuel_cost
                + purchases_cost
            )

            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} "
                f"costs {trip_cost:.2f}"
            )

            if (
                cheapest_cost is None
                or trip_cost < cheapest_cost
            ):
                cheapest_cost = trip_cost
                cheapest_shop = shop

        if customer.money < cheapest_cost:
            print(
                f"{customer.name} "
                f"doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        print(
            f"{customer.name} rides to "
            f"{cheapest_shop.name}"
        )

        customer.location = (
            cheapest_shop.location
        )

        purchase_cost = (
            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart
            )
        )

        distance = customer.distance_to(
            [12, -2]
        )

        fuel_cost = customer.car.trip_cost(
            distance,
            fuel_price
        )

        customer.money -= (
            purchase_cost
            + fuel_cost
        )

        print(
            f"{customer.name} rides home"
        )

        print(
            f"{customer.name} now has "
            f"{customer.money:.2f} dollars"
        )
