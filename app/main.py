from os import path

from app.data_loader import DataLoader
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    data = DataLoader(path.join("app", "config.json"))

    fuel_price = data.fuel_price

    customers = [
        Customer.from_dict(customer_dict)
        for customer_dict in data.customers
    ]

    shops = [Shop.from_dict(shop_dict) for shop_dict in data.shops]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop, trip_cost = customer.pick_cheapest_shop(shops, fuel_price)

        if trip_cost >= customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        customer.ride_to(best_shop, fuel_price)

        customer.ride_home()

        print(f"{customer.name} now has {customer.money} dollars\n")
