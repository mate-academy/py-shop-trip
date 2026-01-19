from app.loaded_data import load_data
from app.utils import calc_distance_cost, calc_purchases_cost


def shop_trip() -> None:
    fuel_price, customers, shops = load_data()

    for customer in customers:
        customer.has_money()
        costs = []

        for shop in shops:
            total_costs = (calc_distance_cost(customer, shop, fuel_price)
                           + calc_purchases_cost(customer, shop))
            total_costs = round(total_costs, 2)
            costs.append((total_costs, shop))
            customer.go_shop(shop.name, total_costs)

        costs_amount, shop = min(costs)

        if costs_amount <= customer.money:
            customer.go_buy(shop.name, costs_amount)
            shop.print_check(customer)
            customer.go_home()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
