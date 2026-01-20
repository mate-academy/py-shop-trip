from app.classes.customer import Customer
from app.classes.shop import Shop


def take_checks(customer: Customer, shops: list[Shop]) -> None:
    if not customer.is_enough_money:
        return
    current_shop = None
    for shop in shops:
        if customer.shop == shop.name:
            current_shop = shop
    print(current_shop.make_check(customer))
