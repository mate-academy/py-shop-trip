from app.customer import Customer
from app.data_processing import shops
from app.cost_calculation import get_fuel_cost, get_product_cost, get_receipt


def chose_shop(
        customer: Customer,
) -> None:

    print(f"{customer.name} has {customer.money} dollars")

    trip_cost_list = [
        get_fuel_cost(customer, shop.location)
        + get_product_cost(customer, shop)
        + get_fuel_cost(customer, customer.home_location)
        for shop in shops
    ]

    for i in range(len(trip_cost_list)):
        print(
            f"{customer.name}'s trip to the {shops[i].name} "
            f"costs {round(trip_cost_list[i], 2)}"
        )

    if min(trip_cost_list) <= customer.money:
        index = trip_cost_list.index(min(trip_cost_list))
        customer.best_shop = shops[index]

        print(f"{customer.name} rides to {customer.best_shop.name}\n")
        get_receipt(customer, customer.best_shop)
        print(f"{customer.name} now has "
              f"{round(customer.money - trip_cost_list[index], 2)} "
              f"dollars\n")
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make a purchase in any shop")
