import datetime

from app.customer import Customer
from app.shop import Shop
from app.user_data import get_data


def shop_trip() -> None:
    customers = [
        Customer(*customer.values())
        for customer in get_data()["customers"]
    ]
    shops = [Shop(*shop.values()) for shop in get_data()["shops"]]
    date = datetime.datetime.now()
    date = date.strftime("%d/%m/%Y %H:%M:%S")

    for customer in customers:
        customer.get_money()
        item_price, shop = customer.product_cost(shops)
        for index, item in enumerate(item_price):
            check_item = str(item).split(".")
            if check_item[-1] == "0":
                item_price[index] = int(check_item[0])
        cost_trip, shop_name, total_coast = shop
        if customer.money > cost_trip:
            counter = 0
            print(f"{customer.name} rides to {shop_name}\n")
            print(f"Date: {date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.product_cart.items():
                print(
                    f"{quantity} {product}s "
                    f"for {item_price[counter]} dollars"
                )
                counter += 1
            print(f"Total cost is {total_coast} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money - cost_trip} dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
