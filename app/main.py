import json
from pathlib import Path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    path_to_file = Path(__file__).parent.joinpath("data/config.json")
    with open(path_to_file) as file:
        source_data = json.load(file)

    Customer.create_customers_from_json(source_data)
    Shop.create_shops_from_json(source_data)

    for customer in Customer.get_customers():
        print(f"{customer.name} has {customer.money} dollars")

        cost_whole_trips = []
        for shop in Shop.get_shops():
            cost_products = customer.cost_products_in_shop(shop)
            cost_drive = customer.cost_drive(shop)
            total_trip_price = cost_drive + cost_products
            cost_whole_trips.append((total_trip_price, shop))

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_trip_price}")

        cheapest_trip_price, cheapest_trip = min(cost_whole_trips)
        if cheapest_trip_price > customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        customer.money -= cheapest_trip_price
        customer.start_trip(cheapest_trip)


if __name__ == "__main__":
    shop_trip()
