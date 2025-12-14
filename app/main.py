import datetime
import json

from app.utils import (
    total_costs,
    shop_registration,
    customers_registration
)


def shop_trip() -> None:

    with open("./app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers_data = data["customers"]
    shops_data = data["shops"]
    customers = customers_registration(customers_data)
    shops = shop_registration(shops_data)

    for customer in customers:

        print(f"{customer.name} has {customer.money} dollars")
        better_cost, better_shop = None, None

        for shop in shops:
            total_cost = total_costs(customer, shop, fuel_price)
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {total_cost}")
            if better_cost is None or better_cost > total_cost:
                better_cost = total_cost
                better_shop = shop

        if customer.money < better_cost:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {better_shop.name}\n")
        home = customer.location
        customer.location = better_shop.location
        today_date = datetime.datetime.now()
        today_date = today_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {today_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0
        for key, value in customer.product_cart.items():
            cost = better_shop.products[key] * value
            cost_print = int(cost) if cost == int(cost) else cost
            print(f"{value} {key}s for {cost_print} dollars")
            total += cost

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        customer.location = home
        customer.money -= better_cost
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
