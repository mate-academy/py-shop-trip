from app.base import create_base
from app.customer import Customer, NotEnoughMoney


def shop_trip() -> None:
    fuel_price, customers, shops = create_base()
    for customer in customers:
        Customer.get_info_customer(customer)
        try:
            cheapest_shop, cheapest_price = Customer.calculate_cheapest_trip(
                customer,
                shops,
                fuel_price
            )
        except NotEnoughMoney:
            continue
        Customer.shop_trip(customer, cheapest_shop)
        Customer.result(customer, cheapest_price)
