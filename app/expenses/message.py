from app.classes.customer import Customer
from app.expenses.trip import trip_expanses, find_shop_to_go, product_expenses


def expanses_report(customer: Customer, shops: list) -> None:
    chosen_shop = find_shop_to_go(customer, shops)
    text = f"{customer.name} has {customer.money} dollars\n"
    for shop in shops:
        text += (f"{customer.name}'s trip "
                 f"to the {shop.name} costs {trip_expanses(customer, shop)}\n")
    money_availability = customer.money - trip_expanses(customer, chosen_shop)
    if money_availability >= 0:
        text += f"{customer.name} rides to {chosen_shop.name}"
        print(text)
        print_receipt(customer, shops)
        print(f"{customer.name} rides home\n{customer.name} "
              f"now has "
              f"{customer.money - trip_expanses(customer, chosen_shop)} "
              f"dollars\n")
    else:
        text += (f"{customer.name} doesn't "
                 f"have enough money to make a purchase in any shop")
        print(text)


def print_receipt(customer: Customer, shops: list) -> None:
    shop = find_shop_to_go(customer, shops)
    price = product_expenses(customer, shop)
    receipt = (
        f"""
Date: 04/01/2021 12:33:41
Thanks, {customer.name}, for your purchase!
You have bought:{' '}
{customer.product_cart.milk} milks for {price['milk']} dollars
{customer.product_cart.bread} breads for {price['bread']} dollars
{customer.product_cart.butter} butters for {price['butter']} dollars
Total cost is {price['total']} dollars
See you again!
"""
    )
    print(receipt)
