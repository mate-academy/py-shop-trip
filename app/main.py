import json
from datetime import datetime
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as file:
        data = json.load(file)
        (_, fuel_price), (_, customers), (_, shops) = data.items()
    customers = [Customer(**customer) for customer in customers]
    shops = [Shop(**shop) for shop in shops]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        maxima, choice, bill = float("inf"), None, None
        for shop in shops:
            buy_coast, check = shop.purchase_cost_for(customer)
            if buy_coast:
                buy_coast = round(buy_coast, 2)
                trip_coast = buy_coast + customer.car.fuel_cost(
                    customer.distance_to(shop), fuel_price)
                print(f"{customer.name}'s trip to the "
                      f"{shop.name} costs {trip_coast}")
                if maxima > trip_coast:
                    if trip_coast <= customer.money:
                        maxima, choice, bill = trip_coast, shop, check

        if choice:
            print(f"{customer.name} rides to {choice.name}")
            print()
            print(f"Date: {datetime.now().strftime("%m/%d/%Y %H:%M:%S")}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought")
            print(bill)
            print("See you again!")
            print()
            print("Bob rides home")
            print(f"Bob now has {customer.money - maxima} dollars")
            print()
        else:
            print("Monica doesn't have enough money "
                  "to make a purchase in any shop")


# Bob has 55 dollars
# Bob's trip to the Outskirts Shop costs 28.21
# Bob's trip to the Shop '24/7' costs 31.48
# Bob rides to Outskirts Shop
#
# Date: 04/01/2021 12:33:41
# Thanks, Bob, for your purchase!
# You have bought:
# 4 milks for 12 dollars
# 2 breads for 2 dollars
# 5 butters for 12.5 dollars
# Total cost is 26.5 dollars
# See you again!
#
# Bob rides home
# Bob now has 26.79 dollars
#
# Monica has 12 dollars
# Monica's trip to the Outskirts Shop costs 15.65
# Monica's trip to the Shop '24/7' costs 16.84
# Monica doesn't have enough money to make a purchase in any shop
if __name__ == "__main__":
    shop_trip()
