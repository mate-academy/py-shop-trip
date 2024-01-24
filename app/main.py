from app.customers_list import customers
from app.shops_list import shops


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        min_trip_cost = float("inf")
        shop_choice = None

        for shop in shops:
            trip_cost = customer.trip_cost(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")
            if min_trip_cost > trip_cost:
                min_trip_cost = trip_cost
                shop_choice = shop

        if min_trip_cost > customer.money:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return

        print(f"{customer.name} rides to {shop_choice.name}")
        customer.print_receipt(shop_choice)

        print(f"{customer.name} rides home")

        customer.money -= min_trip_cost
        print(f"{customer.name} now has {customer.money} dollars\n")
