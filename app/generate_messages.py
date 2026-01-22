import datetime
from typing import List
from app.shop import Shop
from app.customer import Customer


def generate_product_cost_message(item_costs: List) -> str:
    return "\n".join(
        f"{item[1]} {item[0]}s for {item[2]} dollars" for item in item_costs
    )


def generate_return_message(
    customer: Customer,
    money_remainder: float,
    what_have_bought: str,
    total_have_bought: float,
    chosen_shop: Shop
) -> str:

    current_timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if money_remainder >= 0:
        first_message = f"{customer.name} rides to {chosen_shop.name}\n\n"
        initial_customer_location = customer.location

        if first_message:
            customer.location = chosen_shop.location

        second_message = (
            f"Date: {current_timestamp}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: \n"
            f"{what_have_bought}\n"
            f"Total cost is {total_have_bought} dollars\n"
            f"See you again!\n\n"
            f"{customer.name} rides home\n"
        )

        if second_message:
            customer.location = initial_customer_location

        third_message = f"{customer.name} now has {money_remainder} dollars\n"

        return first_message + second_message + third_message

    return (
        f"{customer.name} doesn't have enough money "
        f"to make a purchase in any shop"
    )
