from app.calculations import outskirts_travel_cost, \
    central_travel_cost, shop_24_7_travel_cost, cheapest_trip
from app.variables import customers


def shop_trip():
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        print(f"{customer.name}'s trip to the Outskirts Shop costs "
              f"{outskirts_travel_cost()[customer.name]}\n"
              f"{customer.name}'s trip to the Shop '24/7' costs "
              f"{shop_24_7_travel_cost()[customer.name]}\n"
              f"{customer.name}'s trip to the Central Shop costs "
              f"{central_travel_cost()[customer.name]}")

        if customer.money < min([outskirts_travel_cost()[customer.name],
                                 central_travel_cost()[customer.name],
                                 shop_24_7_travel_cost()[customer.name]]):
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            print(f"{customer.name} rides to "
                  f"{cheapest_trip()[customer.name][0]}")
            print()
            print("Date: 11/03/2020 13:15:34")

            print(f"Thanks, {customer.name}, for your purchase!\n"
                  f"You have bought: \n"
                  f"{customer.product_cart['milk']} milks for "
                  f"{customer.product_price['milk']} dollars\n"
                  f"{customer.product_cart['bread']} breads for "
                  f"{customer.product_price['bread']} dollars\n"
                  f"{customer.product_cart['butter']} butters for "
                  f"{customer.product_price['butter']} dollars")
            print(f"Total cost is {sum(customer.product_price.values())} "
                  f"dollars")
            print("See you again!")
            print()
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{(customer.money - cheapest_trip()[customer.name][1])} "
                  f"dollars")
            print()


shop_trip()
