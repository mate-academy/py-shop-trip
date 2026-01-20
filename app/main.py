import os
import json
from app.shop import Shop
from app.customer import Customer
from app.car import Car


def shop_trip() -> None :
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(**s) for s in config["shops"]]
    customers = []

    for con in config["customers"]:
        car = Car(**con["car"])
        customer = Customer(
            name=con["name"],
            cart=con["product_cart"],
            location=con["location"],
            money=con["money"],
            car=car
        )
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        possible = []
        for shop in shops:
            can_buy, total_cost = customer.can_afford(shop, fuel_price)
            print("{}'s trip to the {} costs {:.2f}".format(
                customer.name, shop.name, round(total_cost, 2)))
            if can_buy:
                possible.append((total_cost, shop))

        if not possible:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
            continue

        best_cost, best_shop = min(possible, key=lambda x: x[0])
        print(f"{customer.name} rides to {best_shop.name}")
        customer.go_to(best_shop.location)

        best_shop.print_receipt(customer.name, customer.cart)

        customer.go_home()
        print(f"{customer.name} rides home")
        customer.money -= round(best_cost, 2)
        print("{} now has {:.2f} dollars\n".format(
            customer.name, round(customer.money, 2)))
