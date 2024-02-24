from app.customers import Customer
from app.shops import Shop
from app.info import get_customers
from app.info import get_shops
from app.trip_cost import trip_cost


shops = Shop.from_dict(get_shops())
customers = Customer.from_dict(get_customers())
trip_prices = trip_cost()


def shop_trip() -> None:
    for i, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")
        for index, shop in enumerate(shops):
            if min(trip_prices[i]) == trip_prices[i][index]:
                low = index
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {trip_prices[i][index]}")
        if customer.money < min(trip_prices[i]):
            print(f"{customer.name}"
                  f" doesn't have enough money to make purchase in any shop")
        else:
            print(f"{customer.name} rides to {shops[low].name}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for you purchase!")
            print("You have bought: ")
            milks = customer.cart["milk"] * shops[low].products["milk"]
            breads = customer.cart["bread"] * shops[low].products["bread"]
            but = customer.cart["butter"] * shops[low].products["butter"]
            print(f"{customer.cart['milk']} milks for {milks} dollars")
            print(f"{customer.cart['bread']} breads for {breads} dollars")
            print(f"{customer.cart['butter']} butters for {but} dollars")
            print(f"Total cost is {milks + breads + but} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has"
                  f" {customer.money - min(trip_prices[i])} dollars\n")
