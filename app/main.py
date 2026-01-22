import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]

    for customer_data in customers_data:
        customer = Customer(**customer_data)

        print(f"{customer.name} has {customer.money} dollars")

        relevant_shop = None
        relevant_shop_trip_costs = float("inf")
        for shop_data in shops_data:
            shop = Shop(**shop_data)
            current_trip_costs = round(
                customer.total_trip_costs(shop, fuel_price),
                2
            )
            if (customer.money >= current_trip_costs
                    and relevant_shop_trip_costs > current_trip_costs):
                relevant_shop = shop
                relevant_shop_trip_costs = current_trip_costs
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {current_trip_costs}")

        if relevant_shop is None:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {relevant_shop.name}\n")

        home_location = customer.location
        customer.location = relevant_shop.location
        relevant_shop.create_receipt(customer.name, customer.product_cart)

        print(f"{customer.name} rides home")
        customer.location = home_location
        money_left = customer.money - relevant_shop_trip_costs
        print(f"{customer.name} now has {money_left} dollars\n")
