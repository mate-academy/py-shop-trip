from app.collect_all_data import (
    calculate_cost_of_trip,
    find_best_trip,
    print_receipt,
    customers,
    shops
)


def shop_trip():
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops.values():
            trip_cost = calculate_cost_of_trip(customer, shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
        if customer.money >= calculate_cost_of_trip(customer, find_best_trip(customer)):
            print(f"{customer.name} rides to {find_best_trip(customer).name}")
            print_receipt(customer, find_best_trip(customer))
            print(f"\n{customer.name} rides home")
            print(
                f"{customer.name} now has {customer.money - calculate_cost_of_trip(customer, find_best_trip(customer))} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
