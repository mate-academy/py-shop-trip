from datetime import datetime

from app.trip_cost import calculate_trip_cost
from app.file_opening import file_open


def shop_trip() -> None:
    user_data = file_open("config.json")
    fuel_price = user_data["fuel_price"]
    customers = user_data["customers"]
    shops = user_data["shops"]
    for customer in customers:
        cheeper_shop = dict()
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            cost = calculate_trip_cost(customer, shop, fuel_price)
            cheeper_shop.update({cost: shop})
            print(f"{customer.name}'s trip "
                  f"to the {shop.name} costs "
                  f"{cost}")
        min_cost = min(list(cheeper_shop.keys()))
        if min_cost <= customer.money:
            customer.location = cheeper_shop[min_cost].location
            print(f"{customer.name} rides to {cheeper_shop[min_cost].name}\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue
        price_all_milks = (cheeper_shop[min_cost].price_milk * customer.milk)
        if price_all_milks == int(price_all_milks):
            price_all_milks = int(price_all_milks)
        price_all_breads = (
            cheeper_shop[min_cost].price_bread * customer.bread
        )
        if price_all_breads == int(price_all_breads):
            price_all_breads = int(price_all_breads)
        price_all_butters = (
            cheeper_shop[min_cost].price_butter * customer.butter
        )
        if price_all_butters == int(price_all_butters):
            price_all_butters = int(price_all_butters)
        total = price_all_breads + price_all_milks + price_all_butters
        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!"
              "\nYou have bought:"
              f"\n{customer.milk} milks for {price_all_milks} dollars"
              f"\n{customer.bread} breads for {price_all_breads} dollars"
              f"\n{customer.butter} butters for {price_all_butters} dollars"
              f"\nTotal cost is {total} dollars"
              f"\nSee you again!\n"
              f"\n{customer.name} rides home\n"
              f"{customer.name} now has {customer.money - min_cost} dollars\n")
