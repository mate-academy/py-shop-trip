from app.initial_data import customers, shops, fuel_price


def shop_trip() -> None:

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = float("inf")
        chosen_shop = None

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            customer.trip_to_the_shop_info(shop, fuel_price)
            if min_cost > cost:
                min_cost = cost
                chosen_shop = shop
        customer.money_comparison_and_shopping(
            min_cost,
            chosen_shop,
            fuel_price
        )
