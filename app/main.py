from app.utils import cheapest_shop, the_cost_of_shopping,\
    calculate_total_cost, cash_balance
from app.data import parse_config


def shop_trip() -> None:
    customers, shops, fuel_price = parse_config("app/config.json")
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop = cheapest_shop(customer, shops, fuel_price)
        if not shop:
            continue
        the_cost_of_shopping(customer, shop, fuel_price)
        calculate_total_cost(customer, shop)
        cash_balance(customer, shop, fuel_price)
