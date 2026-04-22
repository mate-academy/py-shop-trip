from app.config_loader import load_data


def shop_trip() -> None:
    fuel_price, customers, shops = load_data()

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        cheapest_trip_cost = None

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {trip_cost:.2f}"
            )

            if cheapest_trip_cost is None or trip_cost < cheapest_trip_cost:
                cheapest_trip_cost = trip_cost
                cheapest_shop = shop

        if (
            cheapest_trip_cost is None
            or not customer.can_afford(cheapest_trip_cost)
        ):
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            continue

        home_location = customer.location.copy()
        print(f"{customer.name} rides to {cheapest_shop.name}")
        customer.ride_to(cheapest_shop.location)
        cheapest_shop.print_receipt(customer.name, customer.product_cart)
        print(f"{customer.name} rides home")
        customer.ride_to(home_location)
        customer.spend_money(cheapest_trip_cost)
        print(f"{customer.name} now has {customer.money:.2f} dollars")
        print()
