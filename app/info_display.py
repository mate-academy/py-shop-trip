from app.car import Car
from app.info_dict import InfoDict
from app.find_best_shop import find_the_best_shop


def display_info(info_dict: InfoDict) -> None:

    for customer in info_dict.customers:
        car = Car(customer.car)

        print(f"{customer.name} has {customer.money} dollars")

        best_option_shop = find_the_best_shop(
            customer=customer,
            info_dict=info_dict,
            car=car)

        if not best_option_shop:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make purchase in any shop"
            )
            break

        minimal_cost = min(cost for cost in best_option_shop)

        print(f"{customer.name} rides to "
              f"{best_option_shop[minimal_cost].name}\n")

        best_option_shop[minimal_cost].get_receipt(
            customer.name,
            customer.product_cart
        )
        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now "
            f"has {customer.money - minimal_cost} dollars\n"
        )
