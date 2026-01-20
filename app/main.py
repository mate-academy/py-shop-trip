from app.customer import customers
from app.trip import trip_by_car


def shop_trip() -> None:
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        trip_by_car(customer)
