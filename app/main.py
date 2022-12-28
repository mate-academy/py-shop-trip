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
    for i in range(len(customers)):
        trip = []
        for k in range(len(shops)):
            summ = 0
            x1 = customers[i].location[0]
            x2 = shops[k].location[0]
            y1 = customers[i].location[1]
            y2 = shops[k].location[1]
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            for key in shops[k].products:
                summ += customers[i].cart[key] * shops[k].products[key]
            fuel_rate = customers[i].car["fuel_consumption"]
            tr = summ + 2 * dist * fuel_price * fuel_rate / 100
            trip.append(round(tr, 2))
        trip_cost.append(trip)
    for i in range(len(customers)):
        print(f"{customers[i].name} has {customers[i].money} dollars")
        for k in range(len(shops)):
            if min(trip_cost[i]) == trip_cost[i][k]:
                low = k
            print(f"{customers[i].name}'s trip to the"
                  f" {shops[k].name} costs {trip_cost[i][k]}")
        if customers[i].money < min(trip_cost[i]):
            print(f"{customers[i].name}"
                  f" doesn't have enough money to make purchase in any shop")
        else:
            print(f"{customers[i].name} rides to {shops[low].name}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customers[i].name}, for you purchase!")
            print("You have bought: ")
            milks = customers[i].cart["milk"] * shops[low].products["milk"]
            breads = customers[i].cart["bread"] * shops[low].products["bread"]
            but = customers[i].cart["butter"] * shops[low].products["butter"]
            print(f"{customers[i].cart['milk']} milks for {milks} dollars")
            print(f"{customers[i].cart['bread']} breads for {breads} dollars")
            print(f"{customers[i].cart['butter']} butters for {but} dollars")
            print(f"Total cost is {milks + breads + but} dollars")
            print("See you again!\n")
            print(f"{customers[i].name} rides home")
            print(f"{customers[i].name} now has"
                  f" {customers[i].money - min(trip_cost[i])} dollars\n")
