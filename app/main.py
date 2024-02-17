from app.collect_all_data import (
    calculate_cost_of_trip,
    find_best_trip,
    print_receipt,
    customers,
    shops
)


def shop_trip() -> None:
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops.values():
            trip_cost = calculate_cost_of_trip(customer, shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

        best_trip = find_best_trip(customer)
        if customer.money >= calculate_cost_of_trip(customer, best_trip):
            print(f"{customer.name} rides to {best_trip.name}")
            print_receipt(customer, best_trip)
            print(f"\n{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money - calculate_cost_of_trip(
                    customer, best_trip
                )} dollars\n"
            )
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
