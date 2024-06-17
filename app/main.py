import json

from app.shops import Shop
from app.cars import Car
from app.customers import Customer


def shop_trip() -> None:
    list_of_customers = []
    list_of_shops = []

    with open("app/config.json", "r") as file_info:
        all_info = json.load(file_info)

    fuel_price = all_info["FUEL_PRICE"]

    for customer in all_info["customers"]:
        customer_car = Car(customer["car"]["brand"],
                           customer["car"]["fuel_consumption"])

        list_of_customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer_car
            )
        )

    for shop in all_info["shops"]:
        list_of_shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    costs_for_trips = {}

    for customer in list_of_customers:
        print(f"{customer.name} has {customer.money} dollars")
        cost_for_cheapest_trip = 0
        for shop in list_of_shops:
            cost_for_trip = round(
                2 * customer.car.calculate_trip_cost(
                    customer.car.calculate_distance(
                        customer.location,
                        shop.location
                    ),
                    fuel_price
                )
                + shop.calculate_cost_for_products(customer.product_cart)
                , 2
            )
            if cost_for_cheapest_trip == 0:
                cost_for_cheapest_trip = cost_for_trip
                cheapest_shop = shop
            else:
                if cost_for_cheapest_trip > cost_for_trip:
                    cost_for_cheapest_trip = cost_for_trip
                    cheapest_shop = shop
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{cost_for_trip}")
            costs_for_trips[shop] = cost_for_trip

        if min(costs_for_trips.values()) > customer.money:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = shop.location
            cheapest_shop.give_purchase_receipt(customer)
            customer.money -= min(costs_for_trips.values())
            print(f"\n{customer.name} rides home\n{customer.name} "
                  f"now has {customer.money} dollars\n")


shop_trip()
