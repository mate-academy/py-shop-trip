from app.customer import Customer
from app.customer import NotEnoughMoneyException


def shop_trip() -> None:
    customers = Customer.customers_creating()

    for customer in customers:
        customer.print_money()

        try:
            customer.go_to_shop()
        except NotEnoughMoneyException:
            continue

        else:
            customer.making_purchase()
            customer.go_home()
            customer.recount_money()
