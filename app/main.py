from app.trip.trip import Trip
from app.customer.get_customers import get_list_of_customers
from app.shop.get_shops import get_list_of_shops


def shop_trip() -> None:
    shops = get_list_of_shops()
    customers = get_list_of_customers()

    for customer in customers:
        Trip(customer, shops)
