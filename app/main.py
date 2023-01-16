from app.data_file import read_customer_json, read_shop_json, fuel_price
from app.purchase import receipt


def shop_trip() -> None:
    customers = read_customer_json()
    shops = read_shop_json()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        total_cost_in_shop = {}
        for shop in shops:
            total_cost = \
                customer.cost_for_trip_to_the_shop(shop, fuel_price) +\
                customer.product_cost(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")
            total_cost_in_shop.update({total_cost: shop.name})

        min_cost = min(total_cost_in_shop)
        if min_cost <= customer.money:
            print(f"{customer.name} rides to {total_cost_in_shop[min_cost]}\n")
            for shop in shops:
                if shop.name == total_cost_in_shop[min_cost]:
                    receipt(customer, shop)
                    print(f"{customer.name} now has "
                          f"{customer.money - min_cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
