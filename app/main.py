import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        params = json.load(f)

    customers = [Customer.from_dict(cust) for cust in params["customers"]]
    shops = [Shop.from_dict(shop) for shop in params["shops"]]
    fuel_price = params["FUEL_PRICE"]

    for cust in customers:
        print(f"{cust.name} has {cust.money} dollars")
        all_expenses = {}
        for i in range(len(shops)):
            pay_for_trip = cust.pay_for_trip_and_groceries(
                shops[i],
                fuel_price
            )
            print(f"{cust.name}'s trip "
                  f"to the {shops[i].name} costs {pay_for_trip}")
            all_expenses[pay_for_trip] = i
        min_price = min(all_expenses)
        if cust.have_enough_money(min_price):
            shop = shops[all_expenses[min_price]]
            print(f"{cust.name} rides to {shop.name}")
            cust.print_check(shop)
            print(f"{cust.name} rides home")
            cust.pay_for_groceries(min_price)
        else:
            print(f"{cust.name} doesn't have enough "
                  f"money to make a purchase in any shop")
