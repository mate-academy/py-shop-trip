from app.customers import Customer
from app.shops import Shop
from app.info import get_customers
from app.info import get_shops
from app.info import get_fuel_price


fuel_price = get_fuel_price()
shops = Shop.from_dict(get_shops())
customers = Customer.from_dict(get_customers())


def shop_trip() -> None:
    trip_cost = []
    for i, customer in enumerate(customers):
        trip = []
        for i, shop in enumerate(shops):
            summ = 0
            x1 = customer.location[0]
            x2 = shop.location[0]
            y1 = customer.location[1]
            y2 = shop.location[1]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            for key in shop.products:
                summ += customer.cart[key] * shop.products[key]
            fuel_rate = customer.car["fuel_consumption"]
            tr = summ + 2 * dist * fuel_price * fuel_rate / 100
            trip.append(round(tr, 2))
        trip_cost.append(trip)
    for i, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")
        for index, shop in enumerate(shops):
            if min(trip_cost[i]) == trip_cost[i][index]:
                low = index
            print(f"{customer.name}'s trip to the"
                  f" {shop.name} costs {trip_cost[i][index]}")
        if customer.money < min(trip_cost[i]):
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
                  f" {customer.money - min(trip_cost[i])} dollars\n")
