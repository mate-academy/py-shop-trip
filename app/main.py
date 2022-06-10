import datetime
import json
import math


def shop_trip():

    with open("app/config.json", "r") as file_json:
        data = json.load(file_json)
    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    for customer in customers:
        print(f'{customer["name"]} has {customer["money"]} dollars')

        # print: cost of trip to all shops
        costs_table = cost_of_trip_to_shops(customer, shops, fuel_price)
        for shop, total_cost in costs_table.items():
            print(f"{customer['name']}'s trip to the {shop} "
                  f"costs {total_cost:.2f}")

        # print: for what shop customer will drive if he has enough money
        best_shop = min(costs_table, key=costs_table.get)
        if customer["money"] >= costs_table[best_shop]:
            print(f'{customer["name"]} rides to {best_shop}\n')

            # trip to the shop
            home_location = customer["location"]
            for shop in shops:
                if shop["name"] == best_shop:
                    customer["location"] = shop["location"]
                    bill_after_shopping(customer, shop)  # function

            # trip home
            customer["location"] = home_location
            money_ = customer["money"] - costs_table[best_shop]
            print(f'{customer["name"]} rides home\n'
                  f'{customer["name"]} now has {money_:.2f} dollars\n')
        # if customer doesn't have enough money for purchase
        else:
            print(f"{customer['name']} doesn't have "
                  f"enough money to make purchase in any shop")


# function calculate costs_table ans return {"shop": total_cost}
def cost_of_trip_to_shops(customer, shops, fuel_price):
    costs_table = {}

    for shop in shops:
        costs_table[shop["name"]] = fuel_cost(customer, shop, fuel_price)

        for product, value in customer["product_cart"].items():
            costs_table[shop["name"]] += shop["products"][product] * value

    return costs_table


# function calculate cost of fuel for distance to shop and back home
def fuel_cost(customer, shop, fuel_price):
    distance_to_shop = math.dist(customer["location"], shop["location"])
    liter_per_km = customer["car"]["fuel_consumption"] / 100
    price_of_fuel_for_road = distance_to_shop * 2 * fuel_price * liter_per_km
    return price_of_fuel_for_road


# function print bill for purchase
def bill_after_shopping(customer, shop):
    total_bill = 0

    print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
    print(f"Thanks, {customer['name']}, for you purchase!")
    print("You have bought: ")

    for amount, value in customer["product_cart"].items():
        purchase_cost = shop["products"][amount] * value
        print(f'{value} {amount}s for {purchase_cost} dollars')
        total_bill += purchase_cost

    print(f'Total cost is {total_bill} dollars\n'
          f'See you again!\n')


if __name__ == '__main__':
    shop_trip()
