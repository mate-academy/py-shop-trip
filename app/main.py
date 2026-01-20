from app.logic import data_preparing
from app.logic import calculate_trips


def shop_trip() -> None:
    customers, shops, fuel_price = data_preparing("app/config.json")
    calculate_trips(customers, shops, fuel_price)
    for customer in customers:
        customer.print_trips()
