import os
import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    with open(config_path) as json_data_file:
        data = json.load(json_data_file)
        shop_list = [
            Shop(shop["name"], shop["location"], shop["products"])
            for shop in data["shops"]
        ]
        customer_list = [Customer(customer) for customer in data["customers"]]

        for customer in customer_list:
            all_trip_prices = []
            print(f"{customer.name} has {customer.money} dollars")

            for shop in shop_list:
                trip_cost = customer.evaluate_trip(shop, data["FUEL_PRICE"])
                print(
                    f"{customer.name}'s trip to the "
                    f"{shop.name} costs {trip_cost}"
                )
                all_trip_prices.append(trip_cost)

            cheapest_trip_price = min(all_trip_prices)
            index_of_cheapest_trip = all_trip_prices.index(cheapest_trip_price)

            if customer.money >= cheapest_trip_price:
                print(f"{customer.name} rides to "
                      f"{shop_list[index_of_cheapest_trip].name}")
                print("")

                customer.travel_to(shop_list[index_of_cheapest_trip].location)
                cart_cost = shop_list[
                    index_of_cheapest_trip
                ].calculate_cart_cost(customer.product_cart)
                customer.pay(cheapest_trip_price)
                shop_list[index_of_cheapest_trip].print_receipt(
                    customer.name, customer.product_cart, cart_cost
                )

                print(f"{customer.name} rides home")
                print(f"{customer.name} now has {customer.money} dollars")
                print("")
            else:
                print(
                    f"{customer.name} doesn't have enough money to make "
                    f"a purchase in any shop"
                )
