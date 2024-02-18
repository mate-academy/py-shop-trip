from app.data_config import customers, shops, FUEL_PRICE


def shop_trip() -> None:
    for customer in customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        home_location = customer.location
        min_trip_costs = float("inf")
        cheapest_shop = None

        for shop in shops.values():
            shop_distance = shop.calculate_distance_to_shop(customer.location)
            fuel_expense = customer.car.calculate_fuel_expense(shop_distance)
            products_cost = shop.calculate_products_cost(customer.product_cart)
            trip_costs = round(
                fuel_expense * FUEL_PRICE * 2 + products_cost,
                2)
            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {trip_costs}"
            )
            if trip_costs < min_trip_costs:
                min_trip_costs = trip_costs
                cheapest_shop = shop

        if customer.money < min_trip_costs:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            cheapest_shop.make_purchase(customer.name, customer.product_cart)
            print(f"{customer.name} rides home")
            customer.location = home_location
            balance = customer.money - min_trip_costs
            print(f"{customer.name} now has {balance} dollars\n")
