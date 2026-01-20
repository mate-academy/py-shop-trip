import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]

    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ) for customer in config_data["customers"]
    ]

    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in config_data["shops"]
    ]

    for customer in customers:
        cost_of_trips_dict = {}
        for shop in shops:
            total_products_cost = shop.calculate_total_cost(
                customer.products_to_buy,
                shop.product_prices
            )
            total_fuel_cost = customer.car.calculate_fuel_cost(
                customer.location,
                shop.location,
                fuel_price
            )

            cost_of_trips_dict[shop.name] = round(
                total_products_cost + total_fuel_cost * 2,
                2
            )

        cost_of_trips = ""
        target_shop = None
        target_spending_money = min(cost_of_trips_dict.values())

        for shop_name, trip_cost in cost_of_trips_dict.items():
            cost_of_trips += (
                f"{customer.name}'s trip to the {shop_name} "
                f"costs {trip_cost}\n"
            )
            if trip_cost == target_spending_money:
                for shop in shops:
                    if shop.name == shop_name:
                        target_shop = shop

        if customer.money >= target_spending_money:
            remaining_money = customer.money - target_spending_money
            purchase_receipt = target_shop.print_purchase_receipt(
                customer.name,
                customer.products_to_buy,
                target_shop.product_prices
            )
            customer.location = target_shop.location
            print(
                f"{customer.name} has {customer.money} dollars\n"
                f"{cost_of_trips}"
                f"{customer.name} rides to {target_shop.name}\n\n"
                f"{purchase_receipt}\n"
                f"{customer.name} rides home\n"
                f"{customer.name} now has {remaining_money} dollars\n"
            )
        else:
            print(
                f"{customer.name} has {customer.money} dollars\n"
                f"{cost_of_trips}"
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
