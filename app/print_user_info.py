from typing import List

from app.customer import Customer
from app.shop import Shop


def print_user_info(customer: Customer, shops: List[Shop], fuel_price: float) -> None:
    print(f"{customer.name} has {customer.money} dollars")
    cheapest_shop = customer.calculate_trip_costs(shops, fuel_price)
    if cheapest_shop != "not_enough_money":
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.print_bill(customer)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars")
    else:
        print(f"{customer.name} doesn't have enough "
              f"money to make purchase in any shop")