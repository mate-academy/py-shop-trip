import json

from app.car import Car
from app.customers import Customer
from app.shop import Shop

with open("app/config.json", "r") as data_file:
    data = json.load(data_file)


def shop_trip() -> None:
    for customer in data["customers"]:
        customer = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(customer["car"]["brand"],
                    customer["car"]["fuel_consumption"],
                    fuel_price=data["FUEL_PRICE"])
        )
        customer.print_customers_money()

        cost_list = []
        for shop in data["shops"]:
            shop = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            each_shop = []
            trip_cost = (shop.distance_cost(customer, customer.car)
                         + shop.product_costs(customer))
            print(
                f"{customer.name}'s trip to the {shop.name} costs {trip_cost}"
            )
            each_shop.append(shop.name)
            each_shop.append(trip_cost)
            each_shop.append(shop.product_costs(customer))
            cost_list.append(each_shop)

        min_cost = cost_list[0]
        for i, each in enumerate(cost_list):
            if each[1] < min_cost[1]:
                min_cost = cost_list[i]
        if customer.money < min_cost[1]:
            print(f"{customer.name} doesn't have enough money to make purchase"
                  f" in any shop")
        else:
            print(f"{customer.name} rides to {min_cost[0]}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")

            for shop in data["shops"]:
                shop = Shop(
                    name=shop["name"],
                    location=shop["location"],
                    products=shop["products"]
                )
                if shop.name == min_cost[0]:
                    shop.print_purchase(customer)

            print(
                f"Total cost is {min_cost[2]} dollars\n"
                "See you again!\n"
            )
            print(
                f"{customer.name} rides home\n"
                f"{customer.name} now has {customer.money - min_cost[1]} "
                f"dollars\n"
            )
