from decimal import Decimal
from app.customer import Customer


def ride_home(customer: Customer, total_cost: Decimal) -> None:
    print(f"{customer.name} rides home")
    rest_of_money = customer.money - total_cost
    customer.money = rest_of_money
    print(f"{customer.name} now has {rest_of_money} dollars\n"
          f"")
