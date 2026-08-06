import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(customer_data)
        for customer_data in config["customers"]
    ]

    shops = [
        Shop(shop_data)
        for shop_data in config["shops"]
    ]

    for index, customer in enumerate(customers):
        cheapest_shop, cheapest_cost = customer.calculate_cheapest_option(
            shops,
            fuel_price
        )

        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {trip_cost:.2f}"
            )

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            customer.current_location = cheapest_shop.location
            cheapest_shop.print_receipt(customer)

            customer.money -= cheapest_cost

            print(f"{customer.name} rides home")
            customer.current_location = customer.home_location
            print(
                f"{customer.name} now has "
                f"{customer.money:.2f} dollars"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )

        if index < len(customers) - 1:
            print()
