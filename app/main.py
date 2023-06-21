import json

from app.shop import create_shop
from app.customer import create_customer


def shop_trip() -> None:
    data = {}
    for _ in range(3):
        with open("config.json", "r") as data_file:
            data.update(json.load(data_file))
    fuel_price = data["FUEL_PRICE"]
    shops = []
    for shop in data["shops"]:
        shops.append(create_shop(shop))

    customers = []
    for customer in data["customers"]:
        customers.append(create_customer(customer))

    for traveler in customers:
        print(f"{traveler.name} has {traveler.money} dollars")
        costs = {}
        for shop in shops:
            cost = traveler.trip_cost(shop, fuel_price)
            print(f"{traveler.name}'s trip to the {shop.name} costs {cost}")
            costs[cost] = shop
        if min(costs) > traveler.money:
            print(f"{traveler.name} doesn't have enough "
                  "money to make a purchase in any shop")
            continue
        chousen = costs[min(costs)]
        traveler.arrived_to_shop(chousen, min(costs))
        print(f"{traveler.name} rides to {chousen.name}")
        traveler.create_receipt(chousen)
        traveler.remaining_money()
