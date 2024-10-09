from app.components import (
    FUEL_PRICE,
    customers,
    shops,
    show_the_cost_of_purchases
)


def shop_trip() -> None:
    # print(FUEL_PRICE)
    # print(customers)
    # print(shops)
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        show_the_cost_of_purchases(customer, shops, FUEL_PRICE)


shop_trip()
