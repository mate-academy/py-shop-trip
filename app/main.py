from app.service.make_components import (
    FUEL_PRICE,
    customers,
    shops,
)
from app.service.show_the_cost_of_purchases import (
    show_the_cost_of_purchases
)
from app.service.take_checks import take_checks


def shop_trip() -> None:
    for customer in customers:
        customer.print_info()
        show_the_cost_of_purchases(customer, shops, FUEL_PRICE)
        take_checks(customer, shops)
        customer.back_home(shops, FUEL_PRICE)
