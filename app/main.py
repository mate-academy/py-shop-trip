import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    shops_list = [Shop(shop) for shop in config["shops"]]
    customers_list = [Customer(person) for person in config["customers"]]
    for person in customers_list:
        print(f"{person.name} has {person.money} dollars")

        costs = {}
        choosing = {}
        for shop in shops_list:
            costs[shop] = (
                person.fuel_cost(shop, config["FUEL_PRICE"]),
                shop.purchase_receipt(person.product_cart)
            )
            choosing[shop] = costs[shop][0] + sum(costs[shop][1].values())
            print(f"{person.name}'s trip to the {shop.name} "
                  f"costs {round(choosing[shop], 2)}")

        cheapest = min(choosing, key=choosing.get)
        if choosing[cheapest] < person.money:
            person.trip_info(
                cheapest,
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                costs[cheapest][1]
            )
            home_coords = person.coords
            person.coords = cheapest.coords
            person.money -= choosing[cheapest]
            print("Total cost is "
                  f"{round(choosing[cheapest] - costs[cheapest][0],
                           2)} dollars\n"
                  "See you again!\n\n"
                  f"{person.name} rides home\n"
                  f"{person.name} now has {round(person.money, 2)} dollars\n")
            person.coords = home_coords
        else:
            print(f"{person.name} doesn't have enough money "
                  "to make a purchase in any shop")
