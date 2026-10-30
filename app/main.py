import json

from car import Car
from customer import Customer
from shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"],
        )
        for shop in config["shops"]
    ]

    for customer_data in config["customers"]:
        customer = Customer(
            name=customer_data["name"],
            product_cart=customer_data[
                "product_cart"
            ],
            location=customer_data["location"],
            money=customer_data["money"],
            car=Car(
                customer_data["car"]["brand"],
                customer_data["car"][
                    "fuel_consumption"
                ],
            ),
        )

        print(
            f"{customer.name} has "
            f"{customer.money} dollars"
        )

        cheapest_shop = None
        cheapest_cost = None

        for shop in shops:
            distance = customer.distance_to(
                shop.location
            )

            fuel_cost = customer.car.trip_cost(
                distance * 2,
                fuel_price,
            )

            products_cost = (
                shop.products_cost(
                    customer.product_cart
                )
            )

            total_cost = (
                fuel_cost
                + products_cost
            )

            print(
                f"{customer.name}'s trip to "
                f"the {shop.name} costs "
                f"{total_cost:.2f}"
            )

            if (
                cheapest_cost is None
                or total_cost < cheapest_cost
            ):
                cheapest_cost = total_cost
                cheapest_shop = shop

        if (
            cheapest_cost is None
            or customer.money < cheapest_cost
        ):
            print(
                f"{customer.name} doesn't "
                f"have enough money to make "
                f"a purchase in any shop"
            )
            continue

        print(
            f"{customer.name} rides to "
            f"{cheapest_shop.name}"
        )

        home_location = customer.location.copy()

        customer.location = (
            cheapest_shop.location
        )

        products_cost = (
            cheapest_shop.print_receipt(
                customer.name,
                customer.product_cart,
            )
        )

        distance_home = (
            customer.distance_to(
                home_location
            )
        )

        return_fuel_cost = (
            customer.car.trip_cost(
                distance_home,
                fuel_price,
            )
        )

        customer.money -= (
            products_cost
            + return_fuel_cost
        )

        customer.location = home_location

        print(
            f"{customer.name} rides home"
        )

        print(
            f"{customer.name} now has "
            f"{customer.money:.2f} dollars"
        )
