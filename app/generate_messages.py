import datetime
from app.shop import Shop
from typing import List


def generate_product_cost_message(item_costs: List) -> str:
    return "\n".join(
        f"{item[1]} {item[0]}s for {item[2]} dollars" for item in item_costs
    )


def generate_return_message(
    customer_name: str,
    money_remainder: float,
    what_have_bought: str,
    total_have_bought: float,
    chosen_shop: Shop
) -> str:

    current_timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if money_remainder >= 0:
        return (
            f"{customer_name} rides to {chosen_shop.name}\n\n"
            f"Date: {current_timestamp}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought: \n"
            f"{what_have_bought}\n"
            f"Total cost is {total_have_bought} dollars\n"
            f"See you again!\n\n"
            f"{customer_name} rides home\n"
            f"{customer_name} now has {money_remainder} dollars\n"
        )

    return (
        (
            f"{customer_name} doesn't have enough money "
            f"to make a purchase in any shop"
        )
    )
