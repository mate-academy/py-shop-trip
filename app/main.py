import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as data:
        data_in_dict = json.load(data)

    FUEL_PRICE = data_in_dict["FUEL_PRICE"] # noqa

    customers = [Customer(**customer)
                 for customer in data_in_dict["customers"]]
    shops = [Shop(**shop) for shop in data_in_dict["shops"]]

    trip_costs = []

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            trip_costs.append(customer.trip_cost_counter(shop, FUEL_PRICE))
        cheapest_trip = min(trip_costs, key=lambda x: x[1])
        if customer.money >= cheapest_trip[1]:
            print(f"{customer.name} rides to {cheapest_trip[0].name}\n")
            cheapest_trip[0].sell_products(customer)
            customer.money -= cheapest_trip[1]
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
