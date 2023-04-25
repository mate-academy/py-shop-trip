from app.customer import customers
from app.shop import shops


def shop_trip():
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.calculate_cost_trip()
        customer.pick_cheapest_trip()
        if customer.enough_money:
            customer.drives_to_shop()
            customer.buys_products()
            customer.arrives_home()
            customer.counts_remaining_money()
