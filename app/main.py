import json
from app.fuel_costs import fuel_costs
from app.sum_of_shopping import sum_of_shopping
# from datetime import datetime
from app.classes.shop import Shop
from app.classes.customer import Customer


def shop_trip() -> None:

    with open("app/config.json", "r") as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]
    customers_data = [Customer(**customer) for customer in data["customers"]]
    shops_data = [Shop(**shop) for shop in data["shops"]]

    for customer in customers_data:
        print(f"{customer.name} has {customer.money} dollars")
        sums_cost = []
        for shop in shops_data:
            fuel_cost = fuel_costs(
                fuel_price,
                customer.car,
                customer.location,
                shop.location
            )
            shop_costs = sum_of_shopping(customer, shop)
            cost_of_both = shop_costs + fuel_cost
            sums_cost.append(cost_of_both)
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs {cost_of_both}")

        sum_shop = min(sums_cost)
        index_shop = sums_cost.index(sum_shop)
        if sum_shop > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            continue

        print(f"{customer.name} rides "
              f"to {shops_data[index_shop].name}\n")
        time_now = "04/01/2021 12:33:41"
        print(f"Date: {time_now}")
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought: ")
        sum_of_shopping(customer, shops_data[index_shop], print_=True)

        print(f"{customer.name} rides home\n"
              f"{customer.name} now has "
              f"{customer.money - sum_shop} dollars\n")


if __name__ == "__main__":
    shop_trip()
