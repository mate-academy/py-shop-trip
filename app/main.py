from app.config import SHOPS, CUSTOMERS


def shop_trip() -> None:
    for customer in CUSTOMERS:
        choice = [None, customer.balance]
        print(f"{customer.name} has {customer.balance} dollars")
        for shop in SHOPS:
            cost = customer.calculate_trip_cost_to(shop)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            if cost < choice[1]:
                choice = [shop, cost]

        if choice[0] is not None:
            customer.shop_in(*choice)
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  f"purchase in any shop")
