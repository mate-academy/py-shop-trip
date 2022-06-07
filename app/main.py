import json

from app.customers import Customer
from app.shops import Shop


FILE_NAME = "app/config.json"


def shop_trip():
    shops, customers = create_shops_and_customers(FILE_NAME)

    for customer in customers:
        chosen_shop, trip_costs = get_customer_shop(customer, shops)
        if chosen_shop is not None:
            print(f"{customer.name} rides to {chosen_shop}\n")
            chosen_shop.sell_products(customer)
            print(f"{customer.name} rides home")
            left_money = customer.pay_for_trip(trip_costs)
            print(f'{customer.name} now has {left_money} dollars\n')
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")


def get_customer_shop(customer: Customer, shops: list[Shop]):
    print(f"{customer.name} has {customer.money} dollars")

    shops_cost = {}
    for shop in shops:
        costs = customer.trip_costs(shop)
        print(f"{customer.name}'s trip to the {shop.name} costs {costs}")
        shops_cost[costs] = shop
    shops_cost = dict(sorted(shops_cost.items()))

    for costs, shop in shops_cost.items():
        if costs <= customer.money:
            return shop, costs
    return None, None


def create_shops_and_customers(file_name: str):
    with open(file_name) as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    shops = [Shop(item) for item in config_data["shops"]]
    customers = [
        Customer(item, fuel_price)
        for item in config_data["customers"]
    ]

    return shops, customers


if __name__ == '__main__':
    shop_trip()
