from app.information_base import create_lists_customers_shops
from app.customer import Customer, NotEnoughMoney


def shop_trip() -> None:
    fuel_price, customers, shops = create_lists_customers_shops()
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
