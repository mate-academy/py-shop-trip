from app.convertor import customers, shops, fuel_price


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        target_shop, trip_to_shop_cost = customer.pick_cheapest_trip(shops, fuel_price)
        if customer.money >= trip_to_shop_cost:
            customer.drives_to_shop(target_shop)
            customer.drives_home(trip_to_shop_cost)
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  f"purchase in any shop\n")
