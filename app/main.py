from app.json_handling import CUSTOMERS, SHOPS
from app.actions import (choose_shop,
                         sell_products)


def shop_trip() -> None:
    for customer in CUSTOMERS:
        customer.print_money_remainder()
        shop_to_visit = choose_shop(customer, SHOPS)
        if shop_to_visit is None:
            continue
        sell_products(customer, shop_to_visit)
        customer.ride_home_and_show_remainder()


if __name__ == "__main__":

    shop_trip()
