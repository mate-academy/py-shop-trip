from app.trip.get_data import get_data
from app.customer.customer import Customer


def get_list_of_customers() -> list[Customer]:
    """Get a list of customers."""
    customers_list = get_data()["customers"]
    return [Customer(customer) for customer in customers_list]
