import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    customers_data = config["customers"]
    shops_data = config["shops"]
    fuel_price = config["FUEL_PRICE"]

    customers = [Customer(**customer_data) for customer_data in customers_data]
    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost_fuel_for_road = customer.calculate_trip_cost(
                shop.location, fuel_price)
            cost_products = shop.cost_products(customer.product_cart)

            cost_trip = cost_fuel_for_road + cost_products + cost_fuel_for_road
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {cost_trip:.2f}")

            if customer.money >= cost_trip < min_cost:
                min_cost = cost_trip
                cheapest_shop = shop

        if cheapest_shop is not None:
            customer.money -= min_cost

            print(f"{customer.name} rides to {cheapest_shop.name}")

            customer.location = cheapest_shop.location

            print("")
            cheapest_shop.print_receipt(customer.name, customer.product_cart)
            print("")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        if customer != customers[-1]:
            print("")


shop_trip()
