from app.initial_data import customers, shops, fuel_price


def shop_trip() -> None:
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = float("inf")
        chosen_shop = None
        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {customer.calculate_trip_cost(shop, fuel_price)}"
            )
            if min_cost > cost:
                min_cost = cost
                chosen_shop = shop
        if customer.money < min_cost:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            customer.ride_for_products(chosen_shop, fuel_price)
