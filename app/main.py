import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    customers = []
    shops = []

    with open("config.json", "r") as file:
        data = json.load(file)
        for customer in data["customers"]:
            customers.append(Customer.create_customer(customer))

        fuel_price = data["FUEL_PRICE"]

        for shop in data["shops"]:
            shops.append(Shop(name=shop["name"],
                              location=shop["location"],
                              products=shop["products"]))

    for customer in customers:
        available_shops = []
        available_costs = []
        if customers.index(customer) != 0:
            print("")
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:
            trip_cost = customer.get_trip_cost(fuel_price, shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
            available_shops.append(shop)
            available_costs.append(trip_cost)

        chosen_shop = available_shops[available_costs.index(min(available_costs))]
        chosen_cost = available_costs[available_costs.index(min(available_costs))]

        if customer.money < chosen_cost:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {chosen_shop.name}\n")
            customer_home_location = customer.location
            customer.location = chosen_shop.location
            print(chosen_shop.get_receipt(customer.products, customer.name))
            customer.money -= chosen_cost
            print(f"{customer.name} rides home")
            customer.location = customer_home_location
            print(f"{customer.name} now has {customer.money} dollars")

