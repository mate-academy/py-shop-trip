from typing import List

from app.customers.customers import Customer


def creating_customers_classes(customers: List[dict]) -> List[Customer]:
    classes_customers = []
    for customer in customers:
        classes_customers.append(
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=customer["car"]
            )
        )
    return classes_customers
