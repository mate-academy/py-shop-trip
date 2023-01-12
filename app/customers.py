from app.info import get_information


class Customer:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)
        self.car_fuel_consumption_per_km = self.car["fuel_consumption"] / 100


def create_class_instance_customers_list() -> list:
    customers_list = get_information()["customers"]
    customer_class_list = []
    for customer in customers_list:
        customer_class_list.append(Customer(customer))
    return customer_class_list
