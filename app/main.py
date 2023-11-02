from app.initialization import customer_init, shop_init

import json


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    customers = customer_init(data)
    shops = shop_init(data)
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = []
        for shop in shops:
            costs.append(round(customer.calculate_buys(shop, data), 2))
            print(f"{customer.name}'s trip to the {shop.name[0]}"
                  f" costs {round(customer.calculate_buys(shop, data), 2)}")

        cost_index = costs.index(min(costs))
        if customer.money < min(costs):
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {shops[cost_index].name[0]}\n")
        location = customer.location
        customer.location = shops[cost_index].location

        shops[cost_index].print_receipt(customer)
        customer.location = location
        print(f"\n{customer.name} rides home\n{customer.name} now has "
              f"{round(customer.money - min(costs), 2)} dollars\n")
