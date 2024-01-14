import json

from app.customer import Customer
from app.customer import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
        for customer_data in config_data["customers"]:
            customer = Customer(customer_data)
            print(f"{customer.name} has {customer.money} dollars\n")
            cheapest_shop = None
            cheapest_cost = float("inf")

            for shop_data in config_data["shops"]:
                shop = Shop(shop_data)
                trip_cost = customer.calculate_trip_cost(shop)
                if trip_cost < cheapest_cost \
                        and customer.has_enough_money(trip_cost):
                    cheapest_cost = trip_cost
                    cheapest_shop = shop

            if cheapest_shop:
                print(
                    f"{customer.name}'s "
                    f"trip to the {cheapest_shop.name} "
                    f"costs {cheapest_cost:.2f}\n"
                )
                customer.travel_to_shop(cheapest_shop)
                cheapest_shop.sell_products(customer)
                customer.travel_home(trip_cost)
                print(f"{customer.name} rides to {cheapest_shop.name}\n")
            else:
                print(
                    f"{customer.name} "
                    f"doesn't have enough money "
                    f"to make a purchase in any shop\n"
                )


if __name__ == "main":
    shop_trip()
