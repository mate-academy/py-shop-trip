import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict


def create_customer_from_file(data) -> list[Customer]:

    customers_data = data['customers']

    customers = [Customer(
        name=customer['name'],
        product_cart=customer['product_cart'],
        location=customer['location'],
        money=customer['money'],
        car=customer['car']
    ) for customer in customers_data]

    return customers
