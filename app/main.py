import json
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]

    customers = []
    for customer in config["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"])
        )

    shops = []
    for shop in config["shops"]:
        shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"])
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        costs = {}
        for shop in shops:
            cost_trip = (
                Customer.calculate_cost_trip(customer, shop, fuel_price))
            costs[shop] = cost_trip
            print(
                f"{customer.name}'s trip to the {shop.name} costs {cost_trip}"
            )
        chosen_shop = min(costs, key=costs.get)
        if customer.money < (costs[chosen_shop]):
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {chosen_shop.name}\n")

            current_date = (
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Date: {current_date}")
            print(f"Thanks, {customer.name}, for your purchase!\n"
                  "You have bought:")
            total_cost = 0
            for product, amount in customer.product_cart.items():
                price = amount * chosen_shop.products[product]
                if float(price) == int(price):
                    price = int(price)
                total_cost += price
                print(f"{amount} {product}s for {price} dollars")
            money_left = customer.money - (costs[chosen_shop])
            print(f"Total cost is {total_cost} dollars\n"
                  "See you again!\n\n"
                  f"{customer.name} rides home\n"
                  f"{customer.name} now has {money_left} dollars\n")
