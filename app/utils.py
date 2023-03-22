from typing import Dict, List

from app.shop import Shop
from app.customer import Customer


def shopping_choice(
        customer: Customer,
        shop_list: List[Shop],
        fuel_price: int | float
) -> bool:
    print(f"{customer.name} has {customer.money} dollars")

    shop_rating: Dict[int: Shop] = {}
    for shop in shop_list:
        products_cost = shop.products_sum(customer)
        fuel_expense = customer.fuel_costs_calculation(shop, fuel_price)
        travelling_expense = products_cost + fuel_expense
        print(
            f"{customer.name}'s trip to the {shop.name} "
            f"costs {travelling_expense}"
        )
        shop_rating[travelling_expense] = shop

    best_choice = min(shop_rating.keys())
    if customer.money < best_choice:
        print(
            f"{customer.name} doesn't have enough "
            f"money to make a purchase in any shop"
        )
    else:
        selected_shop = shop_rating[best_choice]
        customer.money -= best_choice
        print(f"{customer.name} rides to {selected_shop.name}\n")
        selected_shop.bill(customer)
        return True


def back_home(customer: Customer) -> None:
    print(
        f"{customer.name} rides home\n"
        f"{customer.name} now has {customer.money} dollars\n"
    )
