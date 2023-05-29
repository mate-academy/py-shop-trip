from app.customer import customers, cheapest_shop, the_cost_of_shopping,\
    calculate_total_cost, cash_balance
from app.shop import shops


def shop_trip():
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        the_cost_of_shopping(customer, shops)
        shop = cheapest_shop(customer, shops)
        calculate_total_cost(customer, cheapest_shop(customer, shops))
        cash_balance(customer, shop)
