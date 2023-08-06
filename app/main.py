import datetime
import json

from app.customer import Customer
from app.shop import Shop


def create_shops(shops_data: list[dict]) -> list[Shop]:
    return [Shop(**shop) for shop in shops_data]


def create_customers(customers_data: list[dict]) -> list[Customer]:
    return [Customer(**customer) for customer in customers_data]


def calculate_customers_trip(
        customer: Customer,
        shops: list[Shop],
        fuel_price: float
) -> None:
    print(f"{customer.name} has {customer.money} dollars")

    cheapest_trip_cost = float("inf")
    cheapest_shop = shops[0]

    for shop in shops:
        trip_cost = customer.get_trip_price(shop, fuel_price)
        current_shop = shop
        current_trip_cost = trip_cost

        if trip_cost < cheapest_trip_cost:
            cheapest_shop = shop
            cheapest_trip_cost = trip_cost

        if current_shop == shops[-1] and customer.money < cheapest_trip_cost:
            print(
                f"{customer.name}'s"
                f" trip to the {current_shop.name}"
                f" costs {current_trip_cost:.2f}", end=""
            )
        else:
            print(
                f"{customer.name}'s"
                f" trip to the {current_shop.name}"
                f" costs {current_trip_cost:.2f}"
            )

    if customer.money < cheapest_trip_cost:
        print(f"\n{customer.name}"
              f" doesn't have enough money to make a purchase in any shop"
              )
    else:
        customer.money -= cheapest_trip_cost
        print(f"{customer.name} rides to {cheapest_shop.name}")

        purchase_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        cheapest_shop.print_receipt(customer, purchase_time)

        customer.location = cheapest_shop.location

        print(f"\n{customer.name} rides home")
        print(f"{customer.name} now has {customer.money:.2f} dollars\n")


def shop_trip() -> None:
    with open("app/config.json") as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers_data = config_data["customers"]
    shops_data = config_data["shops"]

    shops = create_shops(shops_data)
    customers = create_customers(customers_data)

    for customer in customers:
        calculate_customers_trip(customer, shops, fuel_price)
