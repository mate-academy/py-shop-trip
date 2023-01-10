import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as data_in:
        data_from_file = json.load(data_in)
        fuel_cost = data_from_file["FUEL_PRICE"]
        customers = [
            Customer(customer) for customer in data_from_file["customers"]
        ]
        shops = [Shop(shop) for shop in data_from_file["shops"]]

        for customer in customers:
            print(f"{customer.name} has {customer.money} dollars")
            dict_shop_and_cost = {}
            for shop in shops:
                cost_to_shop = customer.cost_of_trip_to_shop(
                    shop,
                    fuel_cost
                )
                dict_shop_and_cost[cost_to_shop] = shop
                print(f"{customer.name}'s trip to "
                      f"the {shop.name} costs {cost_to_shop}")

            list_of_trip_costs = [cost for cost in dict_shop_and_cost]
            minimal_cost = list_of_trip_costs[0]
            for cost in dict_shop_and_cost:
                if cost < minimal_cost:
                    minimal_cost = cost

            if customer.money >= minimal_cost:
                customer.go_shopping(
                    dict_shop_and_cost[minimal_cost],
                    fuel_cost
                )

            else:
                print(f"{customer.name} doesn't have enough"
                      f" money to make purchase in any shop")
